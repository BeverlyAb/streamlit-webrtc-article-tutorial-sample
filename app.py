from object_detector import app_object_detection
import streamlit as st

from pathlib import Path

import logging
import threading

from streamlit_webrtc import (
    AudioProcessorBase,
    RTCConfiguration,
    VideoProcessorBase,
    WebRtcMode,
    webrtc_streamer,
)

st.title("KAPI")

RTC_CONFIGURATION = RTCConfiguration(
    {"iceServers": [{"urls": ["stun:stun.l.google.com:19302"]}]}
)
HERE = Path(__file__).parent
logger = logging.getLogger(__name__)


def main():

    object_detection_page = "Real time object detection (sendrecv)"

    app_mode = st.sidebar.selectbox(
        "Choose the app mode",
        [
            object_detection_page,
        ],
    )
    st.subheader(app_mode)
    app_mode = object_detection_page
    if app_mode == object_detection_page:
        app_object_detection(RTC_CONFIGURATION=RTC_CONFIGURATION, HERE=HERE)

    logger.debug("=== Alive threads ===")
    for thread in threading.enumerate():
        if thread.is_alive():
            logger.debug(f"  {thread.name} ({thread.ident})")

main()

