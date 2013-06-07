; Copyright © 2012 Keith Packard <keithp@keithp.com>
; gnet-partslist-bom.scm
; 
; This program is free software; you can redistribute it and/or modify
; it under the terms of the GNU General Public License as published by
; the Free Software Foundation; either version 2 of the License, or
; (at your option) any later version.
; 
; This program is distributed in the hope that it will be useful,
; but WITHOUT ANY WARRANTY; without even the implied warranty of
; MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
; GNU General Public License for more details.
; 
; You should have received a copy of the GNU General Public License
; along with this program; if not, write to the Free Software
; Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA

; The /'s may not work on win32
(load-from-path "gnet-partslist-common.scm")

(define (caddddddr s)
  (car (cdr (cdr (cdr (cdr (cdr (cdr s))))))))

(define (cadddddr s)
  (car (cdr (cdr (cdr (cdr (cdr s)))))))

(define (caddddr s)
  (car (cdr (cdr (cdr (cdr s))))))

(define multiplier 1)

(define (partslist-bom:write-part s port)
  (let ((quantity (caddddddr s))
	(part (cadddddr s))
	(device (cadr s))
	(value (caddr s)))
    (display (* multiplier quantity) port)
    (display "," port)
    (display part port)
    (display "," port)
    (display device port)
    (display " " port)
    (display value port)
    (display "\n" port)))

(define (partslist-bom:write-partslist ls port)
  (if (null? ls)
      '()
      (begin (partslist-bom:write-part (car ls) port)
	     (partslist-bom:write-partslist (cdr ls) port))))

(define (count-same-parts ls)
  (if (null? ls)
      (append ls)
      (let* ((parts-table-no-uref (let ((result '()))
				    (for-each (lambda (l) (set! result (cons (cdr l) result))) (reverse ls))
				    (append result)))
	     (first-ls (car parts-table-no-uref))
	     (match-length (length (member first-ls (reverse parts-table-no-uref))))
	     (rest-ls (list-tail ls match-length))
	     (match-ls (list-tail (reverse ls) (- (length ls) match-length)))
	     (uref-ls (let ((result '()))
			(for-each (lambda (l) (set! result (cons (car l) result))) match-ls)
			(append result))))
	(cons (cons uref-ls (append first-ls  (list match-length))) (count-same-parts rest-ls)))))

(define get-vendor
   (lambda (package)
      (gnetlist:get-package-attribute package "vendor")))

(define get-loadstatus
   (lambda (package)
      (gnetlist:get-package-attribute package "loadstatus")))
  
(define get-vendor-part-number
   (lambda (package)
      (gnetlist:get-package-attribute package "vendor_part_number")))

(define get-footprint
   (lambda (package)
      (gnetlist:get-package-attribute package "footprint")))

(define (get-parts-table-bom packages vendor)
  (if (null? packages)
      '()
      (let ((package (car packages)))
	(if (and (not (string=? (get-loadstatus package) "noload")) (string=? (get-vendor package) vendor))
	    (if (string=? (get-device package) "include")
		(get-parts-table-bom (cdr packages) vendor)
		(cons (list package
			    (get-device package)
			    (get-value package)
			    (get-footprint package)
			    (get-vendor package)
			    (get-vendor-part-number package)) ;; sdb change
		      (get-parts-table-bom (cdr packages) vendor)))
	    (get-parts-table-bom (cdr packages) vendor)))))

(define (get-opt-helper option list)
  (if list
      (let ((param (car list)))
	(if (string-prefix? option (car param))
	    (string-drop (car param) (string-length option))
	    (get-opt-helper option (cdr list))))
      nil)
  )

(define (get-opt option default)
  (let ((opt (get-opt-helper (string-append option "=") (gnetlist:get-calling-flags))))
    (if opt
	opt
	default)))

(define (get-vendor-match)
  (get-opt "vendor" "digikey"))

(define (partslist-bom output-filename)
  (let ((port (open-output-file output-filename))
	(parts-table (marge-sort-with-multikey (get-parts-table-bom packages (get-vendor-match)) '(1 2 3 0))))
    (set! parts-table (count-same-parts parts-table))
    (partslist-bom:write-partslist parts-table port)
    (close-output-port port)))
