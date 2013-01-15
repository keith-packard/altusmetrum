; Copyright (C) 2001-2010 MIYAMOTO Takanori
; gnet-partslist-csv.scm
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

(define partslist-csv:write-top-header
  (lambda (port)
    (display "device,value,footprint,vendor,vendor_part_number,quantity,refdes\n" port)))

(define (partslist-csv:write-partslist ls port)
  (if (null? ls)
      '()
      (begin (write-one-row (cdar ls) "," "," port)
	     (write-one-row (caar ls) " " "\n" port)
	     (partslist-csv:write-partslist (cdr ls) port))))

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

(define get-vendor-part-number
   (lambda (package)
      (gnetlist:get-package-attribute package "vendor_part_number")))

(define get-footprint
   (lambda (package)
      (gnetlist:get-package-attribute package "footprint")))

(define get-loadstatus
  (lambda (package)
    (gnetlist:get-package-attribute package "loadstatus")))

(define (get-parts-table-csv packages)
  (if (null? packages)
      '()
      (let ((package (car packages)))
	(if (string=? (get-device package) "include")
	    (get-parts-table-csv (cdr packages))
	    (if (string=? (get-loadstatus package) "smt")
		(cons (list package
			    (get-device package)
			    (get-value package)
			    (get-footprint package)
			    (get-vendor package)
			    (get-vendor-part-number package)) ;; sdb change
		      (get-parts-table-csv (cdr packages)))
		(get-parts-table-csv (cdr packages)))))))

(define partslist-csv
  (lambda (output-filename)
    (let ((port (open-output-file output-filename))
	  (parts-table (marge-sort-with-multikey (get-parts-table-csv packages) '(1 2 3 0))))
      (set! parts-table (count-same-parts parts-table))
      (partslist-csv:write-top-header port)
      (partslist-csv:write-partslist parts-table port)
      (close-output-port port))))
