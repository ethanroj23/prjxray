# Copyright (C) 2017-2020  The Project X-Ray Authors.
#
# Use of this source code is governed by a ISC-style
# license that can be found in the LICENSE file or at
# https://opensource.org/licenses/ISC
#
# SPDX-License-Identifier: ISC
export XRAY_DATABASE="kintex7"
export XRAY_PART="xc7k70tfbg676-2"
export XRAY_ROI_FRAMES="0x00000000:0xffffffff"

# FIXME: make entire part
export XRAY_ROI_TILEGRID="SLICE_X0Y50:SLICE_X19Y99 DSP48_X0Y20:DSP48_X0Y39 RAMB18_X0Y20:RAMB18_X0Y39 RAMB36_X0Y10:RAMB36_X0Y19"

export XRAY_EXCLUDE_ROI_TILEGRID=""

export XRAY_IOI3_TILES="LIOI3_X0Y9"

# These settings must remain in sync
export XRAY_ROI="SLICE_X0Y50:SLICE_X19Y99 DSP48_X0Y20:DSP48_X0Y39 RAMB18_X0Y20:RAMB18_X0Y39 RAMB36_X0Y10:RAMB36_X0Y19 IOB_X0Y50:IOB_X0Y99"
# Part of CMT X0Y1
export XRAY_ROI_GRID_X1="0"
export XRAY_ROI_GRID_X2="38"
# Include VBRK / VTERM
export XRAY_ROI_GRID_Y1="104"
export XRAY_ROI_GRID_Y2="156"

source $(dirname ${BASH_SOURCE[0]})/../utils/environment.sh

eval $(python3 ${XRAY_UTILS_DIR}/create_environment.py)
