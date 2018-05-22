#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Apr  4 18:27:43 2018

@author: elischwat
"""


import numpy as np
from matplotlib import pyplot as plt
from matplotlib.ticker import FormatStrFormatter
import matplotlib.ticker as ticker


def plotAmpsPhasesVaryingWithH(eta0, lamb, U, g, H, gamma):

  HArr = H
  
  def zNaught(eta0, lamb, U, g, H, gamma):
      alpha = gamma/H; beta = g*H/U**2; omega = 2*np.pi/lamb
      return eta0*(9*alpha**2 + omega**2)/np.sqrt(9*alpha**2 + omega**2*(1-beta)**2)

  def uNaught(eta0, lamb, U, g, H, gamma):
      alpha = gamma/H; beta = g*H/U**2; omega = 2*np.pi/lamb
      return (U/H)*eta0*beta*omega/np.sqrt(9*alpha**2 + omega**2*(1-beta)**2)

  def uPhase(eta0, lamb, U, g, H, gamma):
      alpha = gamma/H; beta = g*H/U**2; omega = 2*np.pi/lamb
      return -np.pi/2 - np.arctan(omega*(1-beta)/(3*alpha))

  def zPhase(eta0, lamb, U, g, H, gamma):
      alpha = gamma/H; beta = g*H/U**2; omega = 2*np.pi/lamb
      return np.arctan(omega/(3*alpha)) - np.arctan(omega*(1-beta)/(3*alpha))    

  plt.subplot(2, 2, 1)
  plt.plot(HArr, zNaught(eta0, lamb, U, g, HArr, gamma))
  ax = plt.gca()
  ax.yaxis.set_major_formatter(FormatStrFormatter('%.00f' + 'm'))
  ax.text(.5,.9,'$\zeta_0$, Fluid Surface Amplitude',
          horizontalalignment='center',
          transform=ax.transAxes, fontsize=15)

  plt.subplot(2, 2, 2)
  plt.plot(HArr, zPhase(eta0, lamb, U, g, HArr, gamma))
  labels = [r'$0$', r'$\frac{1}{2} \pi$', r'$\pi$']
  plt.yticks([0, 1.57075, 3.1415],labels, fontsize=14)
  ax = plt.gca()
  ax.text(.5,.8,'$\phi_\zeta$, Fluid Surface Phase',
          horizontalalignment='center',
          transform=ax.transAxes, fontsize=15)

  plt.subplot(2, 2, 3)
  plt.plot(HArr, uNaught(eta0, lamb, U, g, HArr, gamma))
  plt.xlabel('H, Reach-Averaged Fluid Depth')
  ax = plt.gca()
  ax.yaxis.set_major_formatter(FormatStrFormatter('%.1f' + 'm'))
  ax.text(.5,.9,'$u_0$, Velocity Amplitude',
          horizontalalignment='center',
          transform=ax.transAxes, fontsize=15)

  plt.subplot(2, 2, 4)
  plt.plot(HArr, uPhase(eta0, lamb, U, g, HArr, gamma))
  plt.xlabel('H, Reach-Averaged Fluid Depth')

  labels = [r'$0$', r'$-\frac{1}{2} \pi$']
  plt.yticks([0, -1.57075],labels, fontsize=14)
  ax= plt.gca()
  ax.text(.5,.8,'$\phi_u$, Velocity Phase',
          horizontalalignment='center',
          transform=ax.transAxes, fontsize=15)

  plt.tight_layout()
  plt.show()