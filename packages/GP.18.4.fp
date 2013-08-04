#
# Copyright © 2013 Keith Packard <keithp@keithp.com>
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; version 2 of the License.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License along
# with this program; if not, write to the Free Software Foundation, Inc.,
# 59 Temple Place, Suite 330, Boston, MA 02111-1307 USA.
#

Element(0x00000000 "GP.18.4" "A0" "" 0 0 -8mm -8mm 0 100 0x00000000)
(
	Pin(0mm 1mm 2.50mm 0.50mm 3.00mm 0.95mm "1" "1" 0x00000001)
	ElementLine ( -9mm -9mm  7mm -9mm 15)
	ElementLine (  7mm -9mm  9mm -7mm 15)
	ElementLine (  9mm -7mm  9mm  9mm 15)
	ElementLine (  9mm  9mm -9mm  9mm 15)
	ElementLine ( -9mm  9mm -9mm -9mm 15)

	Pad(0mm 1mm 0mm 1mm 2.5mm 3mm 2.75mm "1" "1" 0x80)
	)
