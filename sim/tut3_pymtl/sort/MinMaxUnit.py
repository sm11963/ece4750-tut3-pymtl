#=========================================================================
# MinMaxUnit
#=========================================================================
# This module takes two inputs, compares them, and outputs the larger
# via the "max" output port and the smaller via the "min" output port.

from pymtl import *
from pclib.rtl import Mux
from pclib.rtl import LtComparator

MUX_LT_SEL_IN0 = 0
MUX_LT_SEL_IN1 = 1
MUX_GT_SEL_IN0 = 1
MUX_GT_SEL_IN1 = 0

class MinMaxUnit( Model ):

  # Constructor

  def __init__( s, nbits=8 ):

    s.in0     = InPort  ( nbits )
    s.in1     = InPort  ( nbits )
    s.out_min = OutPort ( nbits )
    s.out_max = OutPort ( nbits )

    # ''' TUTORIAL TASK ''''''''''''''''''''''''''''''''''''''''''''''''''
    # This model is incomplete. As part of the tutorial you will insert
    # logic here to implement the min/max unit. You should also write a
    # unit test from scratch named MinMaxUnit_test.py.
    # ''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

    s.mux_lt = Mux( nbits, 2 )
    s.mux_gt = Mux( nbits, 2 )

    s.lt_comp = LtComparator( nbits )

    s.connect(s.in0, s.lt_comp.in0)
    s.connect(s.in1, s.lt_comp.in1)
    s.connect_pairs(
      s.mux_gt.sel,    s.lt_comp.out,
      s.mux_gt.in_[0], s.in0,
      s.mux_gt.in_[1], s.in1,
      s.mux_gt.out,    s.out_max
    )
    s.connect_pairs(
      s.mux_lt.sel,    s.lt_comp.out,
      s.mux_lt.in_[1], s.in0,
      s.mux_lt.in_[0], s.in1,
      s.mux_lt.out,    s.out_min
    )


