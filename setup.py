#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""
ObsPy - a Python framework for seismological observatories.

ObsPy is an open-source project dedicated to provide a Python framework for
processing seismological data. It provides parsers for common file formats,
clients to access data centers and seismological signal processing routines
which allow the manipulation of seismological time series (see Beyreuther et
al. 2010, Megies et al. 2011).

The goal of the ObsPy project is to facilitate rapid application development
for seismology.

For more information visit http://www.obspy.org.

:copyright:
    The ObsPy Development Team (devs@obspy.org)
:license:
    GNU Lesser General Public License, Version 3
    (http://www.gnu.org/copyleft/lesser.html)
"""
import distribute_setup
from setuptools import find_packages
from numpy.distutils.core import setup
from numpy.distutils.misc_util import Configuration

import glob
import inspect
import os
import platform
import shutil
import sys

# Directory of the current file in the (hopefully) most reliable way possible.
SETUP_DIRECTORY = os.path.dirname(os.path.abspath(inspect.getfile(
    inspect.currentframe())))

# Import the version string.
UTIL_PATH = os.path.join(SETUP_DIRECTORY, "obspy", "core", "util")
sys.path.append(UTIL_PATH)
from base import _getVersionString  # @UnresolvedImport

LOCAL_PATH = os.path.join(SETUP_DIRECTORY, "setup.py")
DOCSTRING = __doc__.split("\n")

# package specific settings
KEYWORDS = ['ArcLink', 'array', 'array analysis', 'ASC', 'beachball',
    'beamforming', 'cross correlation', 'database', 'dataless',
    'Dataless SEED', 'datamark', 'earthquakes', 'Earthworm', 'EIDA',
    'envelope', 'events', 'features', 'filter', 'focal mechanism', 'GSE1',
    'GSE2', 'hob', 'iapsei-tau', 'imaging', 'instrument correction',
    'instrument simulation', 'IRIS', 'magnitude', 'MiniSEED', 'misfit',
    'mopad', 'MSEED', 'NERA', 'NERIES', 'observatory', 'ORFEUS', 'picker',
    'processing', 'PQLX', 'Q', 'real time', 'realtime', 'RESP',
    'response file', 'RT', 'SAC', 'SEED', 'SeedLink', 'SEG-2', 'SEG Y',
    'SEISAN', 'SeisHub', 'Seismic Handler', 'seismology', 'seismogram',
    'seismograms', 'signal', 'slink', 'spectrogram', 'taper', 'taup',
    'travel time', 'trigger', 'VERCE', 'WAV', 'waveform', 'WaveServer',
    'WaveServerV', 'WebDC', 'Winston', 'XML-SEED', 'XSEED']
INSTALL_REQUIRES = [
    'numpy>1.0.0',
    'scipy',
    'lxml',
    'sqlalchemy',
    'suds>=0.4.0']
ENTRY_POINTS = {
    'console_scripts': [
        'obspy-runtests = obspy.core.scripts.runtests:main',
        'obspy-reftek-rescue = obspy.core.scripts.reftekrescue:main',
        'obspy-indexer = obspy.db.scripts.indexer:main',
        'obspy-scan = obspy.imaging.scripts.scan:main',
        'obspy-plot = obspy.imaging.scripts.plot:main',
        'obspy-mopad = obspy.imaging.scripts.mopad:main',
        'obspy-mseed-recordanalyzer = obspy.mseed.scripts.recordanalyzer:main',
        'obspy-dataless2xseed = obspy.xseed.scripts.dataless2xseed:main',
        'obspy-xseed2dataless = obspy.xseed.scripts.xseed2dataless:main',
        'obspy-dataless2resp = obspy.xseed.scripts.dataless2resp:main',
    ],
    'obspy.plugin.waveform': [
        'TSPAIR = obspy.core.ascii',
        'SLIST = obspy.core.ascii',
        'PICKLE = obspy.core.stream',
        'DATAMARK = obspy.datamark.core',
        'GSE1 = obspy.gse2.core',
        'GSE2 = obspy.gse2.core',
        'MSEED = obspy.mseed.core',
        'SAC = obspy.sac.core',
        'SACXY = obspy.sac.core',
        'SEG2 = obspy.seg2.seg2',
        'SEGY = obspy.segy.core',
        'SU = obspy.segy.core',
        'SEISAN = obspy.seisan.core',
        'Q = obspy.sh.core',
        'SH_ASC = obspy.sh.core',
        'WAV = obspy.wav.core',
    ],
    'obspy.plugin.waveform.TSPAIR': [
        'isFormat = obspy.core.ascii:isTSPAIR',
        'readFormat = obspy.core.ascii:readTSPAIR',
        'writeFormat = obspy.core.ascii:writeTSPAIR',
    ],
    'obspy.plugin.waveform.SLIST': [
        'isFormat = obspy.core.ascii:isSLIST',
        'readFormat = obspy.core.ascii:readSLIST',
        'writeFormat = obspy.core.ascii:writeSLIST',
    ],
    'obspy.plugin.waveform.PICKLE': [
        'isFormat = obspy.core.stream:isPickle',
        'readFormat = obspy.core.stream:readPickle',
        'writeFormat = obspy.core.stream:writePickle',
    ],
    'obspy.plugin.waveform.DATAMARK': [
        'isFormat = obspy.datamark.core:isDATAMARK',
        'readFormat = obspy.datamark.core:readDATAMARK',
    ],
    'obspy.plugin.waveform.GSE1': [
        'isFormat = obspy.gse2.core:isGSE1',
        'readFormat = obspy.gse2.core:readGSE1',
    ],
    'obspy.plugin.waveform.GSE2': [
        'isFormat = obspy.gse2.core:isGSE2',
        'readFormat = obspy.gse2.core:readGSE2',
        'writeFormat = obspy.gse2.core:writeGSE2',
    ],
    'obspy.plugin.waveform.MSEED': [
        'isFormat = obspy.mseed.core:isMSEED',
        'readFormat = obspy.mseed.core:readMSEED',
        'writeFormat = obspy.mseed.core:writeMSEED',
    ],
    'obspy.plugin.waveform.SAC': [
        'isFormat = obspy.sac.core:isSAC',
        'readFormat = obspy.sac.core:readSAC',
        'writeFormat = obspy.sac.core:writeSAC',
    ],
    'obspy.plugin.waveform.SACXY': [
        'isFormat = obspy.sac.core:isSACXY',
        'readFormat = obspy.sac.core:readSACXY',
        'writeFormat = obspy.sac.core:writeSACXY',
    ],
    'obspy.plugin.waveform.SEG2': [
        'isFormat = obspy.seg2.seg2:isSEG2',
        'readFormat = obspy.seg2.seg2:readSEG2',
        'writeFormat = obspy.seg2.seg2:writeSEG2',
    ],
    'obspy.plugin.waveform.SEGY': [
        'isFormat = obspy.segy.core:isSEGY',
        'readFormat = obspy.segy.core:readSEGY',
        'writeFormat = obspy.segy.core:writeSEGY',
    ],
    'obspy.plugin.waveform.SU': [
        'isFormat = obspy.segy.core:isSU',
        'readFormat = obspy.segy.core:readSU',
        'writeFormat = obspy.segy.core:writeSU',
    ],
    'obspy.plugin.waveform.SEISAN': [
        'isFormat = obspy.seisan.core:isSEISAN',
        'readFormat = obspy.seisan.core:readSEISAN',
    ],
    'obspy.plugin.waveform.Q': [
        'isFormat = obspy.sh.core:isQ',
        'readFormat = obspy.sh.core:readQ',
        'writeFormat = obspy.sh.core:writeQ',
    ],
    'obspy.plugin.waveform.SH_ASC': [
        'isFormat = obspy.sh.core:isASC',
        'readFormat = obspy.sh.core:readASC',
        'writeFormat = obspy.sh.core:writeASC',
    ],
    'obspy.plugin.waveform.WAV': [
        'isFormat = obspy.wav.core:isWAV',
        'readFormat = obspy.wav.core:readWAV',
        'writeFormat = obspy.wav.core:writeWAV',
    ],
    'obspy.plugin.event': [
        'QUAKEML = obspy.core.quakeml',
    ],
    'obspy.plugin.event.QUAKEML': [
        'isFormat = obspy.core.quakeml:isQuakeML',
        'readFormat = obspy.core.quakeml:readQuakeML',
        'writeFormat = obspy.core.quakeml:writeQuakeML',
    ],
    'obspy.plugin.detrend': [
        'linear = scipy.signal:detrend',
        'constant = scipy.signal:detrend',
        'demean = scipy.signal:detrend',
        'simple = obspy.signal.detrend:simple',
    ],
    'obspy.plugin.differentiate': [
        'gradient = numpy:gradient',
    ],
    'obspy.plugin.filter': [
        'bandpass = obspy.signal.filter:bandpass',
        'bandstop = obspy.signal.filter:bandstop',
        'lowpass = obspy.signal.filter:lowpass',
        'highpass = obspy.signal.filter:highpass',
        'lowpassCheby2 = obspy.signal.filter:lowpassCheby2',
        'lowpassFIR = obspy.signal.filter:lowpassFIR',
        'remezFIR = obspy.signal.filter:remezFIR',
    ],
    'obspy.plugin.integrate': [
        'trapz = scipy.integrate:trapz',
        'cumtrapz = scipy.integrate:cumtrapz',
        'simps = scipy.integrate:simps',
        'romb = scipy.integrate:romb',
    ],
    'obspy.plugin.taper': [
        'cosine = obspy.signal.invsim:cosTaper',
        'barthann = scipy.signal:barthann',
        'bartlett = scipy.signal:bartlett',
        'blackman = scipy.signal:blackman',
        'blackmanharris = scipy.signal:blackmanharris',
        'bohman = scipy.signal:bohman',
        'boxcar = scipy.signal:boxcar',
        'chebwin = scipy.signal:chebwin',
        'flattop = scipy.signal:flattop',
        'gaussian = scipy.signal:gaussian',
        'general_gaussian = scipy.signal:general_gaussian',
        'hamming = scipy.signal:hamming',
        'hann = scipy.signal:hann',
        'kaiser = scipy.signal:kaiser',
        'nuttall = scipy.signal:nuttall',
        'parzen = scipy.signal:parzen',
        'slepian = scipy.signal:slepian',
        'triang = scipy.signal:triang',
    ],
    'obspy.plugin.trigger': [
        'recstalta = obspy.signal.trigger:recSTALTA',
        'carlstatrig = obspy.signal.trigger:carlSTATrig',
        'classicstalta = obspy.signal.trigger:classicSTALTA',
        'delayedstalta = obspy.signal.trigger:delayedSTALTA',
        'zdetect = obspy.signal.trigger:zDetect',
        'recstaltapy = obspy.signal.trigger:recSTALTAPy',
        'classicstaltapy = obspy.signal.trigger:classicSTALTAPy',
    ],
    'obspy.db.feature': [
        'minmax_amplitude = obspy.db.features:MinMaxAmplitudeFeature',
        'bandpass_preview = obspy.db.features:BandpassPreviewFeature',
    ],
}


def convert2to3():
    """
    Convert source to Python 3.x syntax using lib2to3.
    """
    # create a new 2to3 directory for converted source files
    dst_path = os.path.join(LOCAL_PATH, '2to3')
    shutil.rmtree(dst_path, ignore_errors=True)

    # copy original tree into 2to3 folder ignoring some unneeded files
    def ignored_files(adir, filenames):  # @UnusedVariable
        return ['.svn', '2to3', 'debian', 'build', 'dist'] + \
               [fn for fn in filenames if fn.startswith('distribute')] + \
               [fn for fn in filenames if fn.endswith('.egg-info')]
    shutil.copytree(LOCAL_PATH, dst_path, ignore=ignored_files)
    os.chdir(dst_path)
    sys.path.insert(0, dst_path)
    # run lib2to3 script on duplicated source
    from lib2to3.main import main
    print("Converting to Python3 via lib2to3...")
    main("lib2to3.fixes", ["-w", "-n", "--no-diffs", "obspy"])


def _get_lib_name(lib):
    return "lib%s_%s_%s_py%s" % (lib, platform.system(),
        platform.architecture()[0], "".join([str(i) for i in
            platform.python_version_tuple()[:2]]))


def setupPackage():
    # automatically install distribute if the user does not have it installed
    distribute_setup.use_setuptools()
    # use lib2to3 for Python 3.x
    if sys.version_info[0] == 3:
        convert2to3()

    def configuration(parent_package="", top_path=None):
        config = Configuration("", parent_package, top_path)

        # Add obspy.taup source files.
        obspy_taup_dir = os.path.join(SETUP_DIRECTORY, "obspy", "taup")
        # Hack to get a architecture specific taup library filename.
        libname = _get_lib_name("tau")
        new_interface_path = os.path.join("build", libname + os.extsep + "pyf")
        interface_file = os.path.join(obspy_taup_dir, "src", "_libtau.pyf")
        with open(interface_file, "r") as open_file:
            interface_file = open_file.read()
        # In the original .pyf file the library is called _libtau.
        interface_file = interface_file.replace("_libtau", libname)
        print interface_file

        if not os.path.exists("build"):
            os.mkdir("build")
        with open(new_interface_path, "w") as open_file:
            open_file.write(interface_file)
        taup_files = glob.glob(os.path.join(obspy_taup_dir, "src", "*.f"))
        taup_files.insert(0, new_interface_path)
        config.add_extension(libname, taup_files)

        # Add obspy.gse2 source files.
        gse2_src_path = os.path.join(SETUP_DIRECTORY, "obspy", "gse2", "src",
            "GSE_UTI")
        gse2_files = [os.path.join(gse2_src_path, "buf.c"),
            os.path.join(gse2_src_path, "gse_functions.c")]
        config.add_extension(_get_lib_name("gse2"), gse2_files)

        # Add obspy.mseed source files.
        mseed_src_path = os.path.join(SETUP_DIRECTORY, "obspy", "mseed", "src")
        mseed_src_files = glob.glob(os.path.join(mseed_src_path, "libmseed",
            "*.c"))
        mseed_src_files.append(os.path.join(mseed_src_path,
            "obspy-readbuffer.c"))
        config.add_extension(_get_lib_name("mseed"), mseed_src_files)

        # Add obspy.segy source files.
        segy_files = [os.path.join(SETUP_DIRECTORY, "obspy", "segy", "src",
            "ibm2ieee.c")]
        config.add_extension(_get_lib_name("segy"), segy_files)

        # Add obspy.signal source code files.
        signal_src_path = os.path.join(SETUP_DIRECTORY, "obspy", "signal",
            "src")
        signal_src_files = glob.glob(os.path.join(signal_src_path, "*.c"))
        signal_src_files.extend(glob.glob(os.path.join(signal_src_path, "fft",
            "*.c")))
        config.add_extension(_get_lib_name("signal"), signal_src_files)

        # Add evalresp source files.
        src_evresp = glob.glob(os.path.join("obspy", "signal", "src",
            "evalresp", "*.c"))
        config.add_extension(_get_lib_name("evresp"), src_evresp)

        return config

    # setup package
    setup(
        name='obspy',
        version=_getVersionString(),
        description=DOCSTRING[1],
        long_description="\n".join(DOCSTRING[3:]),
        url="http://www.obspy.org",
        author='The ObsPy Development Team',
        author_email='devs@obspy.org',
        license='GNU Lesser General Public License, Version 3 (LGPLv3)',
        platforms='OS Independent',
        classifiers=[
            'Development Status :: 4 - Beta',
            'Environment :: Console',
            'Intended Audience :: Science/Research',
            'Intended Audience :: Developers',
            'License :: OSI Approved :: GNU Library or ' +
                'Lesser General Public License (LGPL)',
            'Operating System :: OS Independent',
            'Programming Language :: Python',
            'Topic :: Scientific/Engineering',
            'Topic :: Scientific/Engineering :: Physics'],
        keywords=KEYWORDS,
        packages=find_packages(exclude=['distribute_setup']),
        namespace_packages=[],
        zip_safe=False,
        install_requires=INSTALL_REQUIRES,
        download_url="https://github.com/obspy/obspy/zipball/master",
        include_package_data=True,
        entry_points=ENTRY_POINTS,
        ext_package='obspy.lib',
        use_2to3=True,
        configuration=configuration,
    )
    # cleanup after using lib2to3 for Python 3.x
    if sys.version_info[0] == 3:
        os.chdir(LOCAL_PATH)

if __name__ == '__main__':
    setupPackage()
