;;; Altus Metrum CSV part list plug-in for lepton-netlist
;;; Copyright (C) 2018 Bdale Garbee
;;;
;;; This program is free software; you can redistribute it and/or modify
;;; it under the terms of the GNU General Public License as published by
;;; the Free Software Foundation; either version 2 of the License, or
;;; (at your option) any later version.
;;;
;;; This program is distributed in the hope that it will be useful,
;;; but WITHOUT ANY WARRANTY; without even the implied warranty of
;;; MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
;;; GNU General Public License for more details.
;;;
;;; You should have received a copy of the GNU General Public License
;;; along with this program; if not, write to the Free Software
;;; Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
;;; MA 02111-1301 USA.

;; --------------------------------------------------------------------------
;; This program generates a bill of materials in Altus Metrum format.  
;;
;; You must have a file 'attribs' in the project directory with one attribute
;; per line of all the attributes you want included, no comments allowed.
;;
;; The output consists of comma-separated fields for each of the attributes
;; per part, quantity of that part, and a space-separated list of refdes.
;;
;; This program is inspired by the 'bom2' netlist module initially written
;; by Matt Ettus.
;; --------------------------------------------------------------------------

(use-modules (ice-9 rdelim)
             (gnetlist backend-getopt)
             (gnetlist schematic)
             (srfi srfi-26))

(define bomAM:open-input-file
  (lambda (options)
    (let ((filename (backend-option-ref options 'attrib_file "attribs")))
      (if (file-exists? filename)
          (open-input-file filename)
          (if (backend-option-ref options 'attribs) #f
              (begin
                (format (current-error-port)
"ERROR: Attribute file '~A' not found. You must do one of the following:\n"
"         - Create an 'attribs' file\n"
"         - Specify an attribute file using -Oattrib_file=<filename>\n"
"         - Specify which attributes to include using -Oattribs=attrib1,attrib2,... (no spaces)\n"
filename)
                (primitive-exit 1)))))))

(define bomAM
  (lambda (output-filename)
    (let* ((options (backend-getopt
                     (gnetlist:get-backend-arguments)
                     '((attrib_file (value #t)) (attribs (value #t)))))
           (attriblist (bomAM:parseconfig (bomAM:open-input-file options) options)))
      (and attriblist
           (begin
             (bomAM:printlist (append attriblist (list "quantity" "refdes")) #\,)
             (newline)
             (bomAM:printbom (bomAM:components (schematic-packages toplevel-schematic)
                                             attriblist)
                            0))))))

(define bomAM:printbom
  (lambda (bomlist count)
    (if (not (null? bomlist))
      (if (not (null? (caar bomlist)))
        (begin
          (bomAM:printlist (cdar bomlist) #\,)
          (display #\,)
          (bomAM:printcount bomlist 0)
          (display #\,)
          (bomAM:printrefdes bomlist 0)
          (newline)
          (bomAM:printbom (cdr bomlist) 0)
        )))))

(define bomAM:printcount
  (lambda (bomlist count)
    (if (not (null? bomlist))
      (if (not (null? (caar bomlist)))
        (begin
          (bomAM:printcount (cons (cons (cdaar bomlist)(cdar bomlist))(cdr bomlist)) (+ count 1))
	)
        (display count)
      ))))

(define bomAM:printrefdes
  (lambda (bomlist count)
    (if (not (null? bomlist))
      (if (not (null? (caar bomlist)))
        (begin
          (display (caaar bomlist))
          (if (not (null? (cdaar bomlist)))
            (write-char #\  ))
          (bomAM:printrefdes (cons (cons (cdaar bomlist)(cdar bomlist))(cdr bomlist)) (+ count 1))
)))))

(define bomAM:printlist
  (lambda (ls delimiter)
    (if (null? ls)
        #f
        (begin
          (display (car ls))
          (if (not (null? (cdr ls)))
            (write-char delimiter))
          (bomAM:printlist (cdr ls) delimiter)))))

; Parses attrib file. Returns a list of read attributes.
(define bomAM:parseconfig
  (lambda (port options)
    (let ((attribs (backend-option-ref options 'attribs)))
      (if attribs (string-split attribs #\,)
          (and port
               (let ((read-from-file (read-delimited " \n\t" port)))
                 (cond ((eof-object? read-from-file)
                        '())
                       ((= 0 (string-length read-from-file))
                        (bomAM:parseconfig port options))
                       (else
                        (cons read-from-file (bomAM:parseconfig port options))))))))))

(define bomAM:match-list?
  (lambda (l1 l2)
    (cond
      ((and (null? l1)(null? l2))#t)
      ((null? l1) #f)
      ((null? l2) #f)
      ((not (string=? (car l1)(car l2)))#f)
      (#t (bomAM:match-list? (cdr l1)(cdr l2))))))

(define bomAM:match?
  (lambda (uref attriblist bomlist)
    (if (null? bomlist)
      (list (cons (list uref) attriblist))
      (if (bomAM:match-list? attriblist (cdar bomlist))
        (cons (cons (merge (list uref) (caar bomlist) string<? ) (cdar bomlist))(cdr bomlist))
        (cons (car bomlist)(bomAM:match? uref attriblist (cdr bomlist)))))))

(define (bomAM:in-bom? package)
  (string=? "unknown"
            (gnetlist:get-package-attribute package "nobom")))

(define (bomAM:components-impl ls attriblist bomlist)
  (if (null? ls)
      bomlist
      (let* ((package (car ls))
             (attribs (bomAM:find-attribs package attriblist)))
        (bomAM:components-impl (cdr ls) attriblist
                              (if (bomAM:in-bom? package)
                                  (bomAM:match? package attribs bomlist)
                                  bomlist)))))

(define (bomAM:components ls attriblist)
   (bomAM:components-impl ls attriblist '()))

(define (bomAM:find-attribs package attriblist)
  (map (cut gnetlist:get-package-attribute package <>) attriblist))

