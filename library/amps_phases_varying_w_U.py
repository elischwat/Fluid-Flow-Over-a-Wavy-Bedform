#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Apr  3 00:56:09 2018

@author: elischwat
"""


import numpy as np
from matplotlib import pyplot as plt
from matplotlib.ticker import FormatStrFormatter
import matplotlib.ticker as ticker

def plotAmpsPhasesVaryingWithU(eta0, lamb, U, g, H, gamma):

  UArr = U

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
  plt.plot(UArr, zNaught(eta0, lamb, UArr, g, H, gamma))
  plt.xlim(0), plt.ylim(0)
  ax = plt.gca()
  ax.yaxis.set_major_formatter(FormatStrFormatter('%.1f' + 'm'))
  ax.text(.6,.9,'$\zeta_0$, Fluid Surface Amplitude',
          horizontalalignment='center',
          transform=ax.transAxes, fontsize=15)

  plt.subplot(2, 2, 2)
  plt.plot(UArr, zPhase(eta0, lamb, UArr, g, H, gamma))
  #plt.xlim(0), plt.ylim(0)
  labels = [r'$0$', r'$\frac{1}{2} \pi$', r'$\pi$']
  plt.yticks([0, 1.57075, 3.1415],labels, fontsize=14)
  ax = plt.gca()
  ax.text(.6,.9,'$\phi_\zeta$, Fluid Surface Phase',
          horizontalalignment='center',
          transform=ax.transAxes, fontsize=15)


  plt.subplot(2, 2, 3)
  plt.plot(UArr, uNaught(eta0, lamb, UArr, g, H, gamma))
  plt.xlabel('U, Reach-Averaged Fluid Velocity')
  plt.xlim(0), plt.ylim(0)
  ax = plt.gca()
  ax.yaxis.set_major_formatter(FormatStrFormatter('%.1f' + 'm'))
  ax.text(.6,.9,'$u_0$, Velocity Amplitude',
          horizontalalignment='center',
          transform=ax.transAxes, fontsize=15)

  plt.subplot(2, 2, 4)
  plt.plot(UArr, uPhase(eta0, lamb, UArr, g, H, gamma))
  plt.xlabel('U, Reach-Averaged Fluid Velocity')
  labels = [r'$0$', r'-$\frac{1}{2} \pi$', r'-$\pi$']
  plt.yticks([0, -1.57075, -3.1415],labels, fontsize=14)
  ax = plt.gca()
  ax.text(.6,.9,'$\phi_u$, Velocity Phase',
          horizontalalignment='center',
          transform=ax.transAxes, fontsize=15)

  plt.tight_layout()
  plt.show()