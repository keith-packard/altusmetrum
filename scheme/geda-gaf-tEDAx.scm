;;; tEDAx plug-in for gnetlist
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

;;
;; returns the device attribute value
;;
(define tEDAx:get-device
   (lambda (package)
      (gnetlist:get-package-attribute package "device")))

;;
;; returns the footprint attribute value (PATTERN if not defined)
;;
(define tEDAx:get-pattern
   (lambda (package)
      (define pattern (gnetlist:get-package-attribute package "footprint"))
      (if (string=? "unknown" pattern)
         "PATTERN"
         pattern)))
; how do i return "PATTERN" if not defined? humm... need to read some
; guile stuff... i did, and see the result :)

;;
;; returns the value attribute (empty if not defined)
;;
(define tEDAx:get-value
   (lambda (package)
      (define value (gnetlist:get-package-attribute package "value"))
      (if (string=? "unknown" value)
         ""
	 value)))
 
;;
;; header
;;
(define tEDAx:header
   (lambda (port)
      (display "tEDAx v1" port) 
      (newline port)

      (display "begin netlist v1 netlist" port)
      (newline port)
      (newline port)))

;;
;; trailer
;;
(define tEDAx:trailer
   (lambda (port)
      (display "end netlist" port) 
      (newline port)))

;;
;; component related lines 
;;
(define tEDAx:components
   (lambda (port ls)
      (if (not (null? ls))
         (let ((package (car ls)))
            (begin
               (display "\tfootprint " port)
               (display package port)
               (display " " port)
               (display (tEDAx:get-pattern package) port)
               (newline port)

               (display "\tdevice " port)
               (display package port)
               (display " " port)
               (display (tEDAx:get-device package) port)
               (newline port)

               (display "\tvalue " port)
               (display package port)
               (display " " port)
               (display (tEDAx:get-value package) port)
               (newline port)

               (newline port)
               (tEDAx:components port (cdr ls)))))))

(define (tEDAx:pinfmt pin)
  (format #f "~a ~a" (car pin) (car (cdr pin)))
  )

(define (tEDAx:each-pin net pins port)
  (if (not (null? pins))
      (let ((pin (car pins)))
        (format port "\tconn ~a ~a~%" net (tEDAx:pinfmt pin))
        (tEDAx:each-pin net (cdr pins) port))))

;;
;; network related lines 
;;
(define (tEDAx:each-net netnames port)
  (if (not (null? netnames))
      (let ((netname (car netnames)))
        (tEDAx:each-pin netname (gnetlist:get-all-connections netname) port)
        (tEDAx:each-net (cdr netnames) port))))

;;; 
;;; output a tEDAx formatted netlist
;;;
(define tEDAx
   (lambda (output-filename)
      (let ((port (open-output-file output-filename)))
         (begin
	    (tEDAx:header port)
	    (tEDAx:components port packages)
	    (tEDAx:each-net (gnetlist:get-all-unique-nets "dummy") port)
	    (tEDAx:trailer port))
	 (close-output-port port))))

;; --------------------------------------------------------------------------

