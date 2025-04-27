import streamlit as st
import numpy as np
import scipy.io.wavfile
import tempfile
from st_audiorec import st_audiorec

st.title("\ud83c\udfa4 \u9332\u97f3\u30c0\u30a6\u30f3\u30ed\u30fc\u30c9\u5c02\u7528\u30a2\u30d7\u30ea (Streamlit Cloud\u7528)")

st.write("\n\ud83d\udc49 \u4e0b\u306e\u9332\u97f3\u30dc\u30bf\u30f3\u3092\u62bc\u3057\u3066\u3001\u8a18\u9304\u3092\u958b\u59cb\u3057\u307e\u3059\uff01")

# 録音ウィジェット
wav_audio_data = st_audiorec()

if isinstance(wav_audio_data, np.ndarray):
    st.success("\u9332\u97f3\u5b8c\u4e86！\u30c0\u30a6\u30f3\u30ed\u30fc\u30c9で\u304dま\u3059\uff01")

    # 一時ファイルに録音を保存
    with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as tmp_wav:
        scipy.io.wavfile.write(tmp_wav.name, 44100, wav_audio_data)
        audio_file_path = tmp_wav.name

    # ダウンロードボタン
    with open(audio_file_path, "rb") as f:
        st.download_button(
            label="\ud83d\udce5 \u9332\u97f3\u30c7\u30fc\u30bf\u3092\u30c0\u30a6\u30f3\u30ed\u30fc\u30c9",
            data=f,
            file_name="recorded_audio.wav",
            mime="audio/wav"
        )
else:
    st.info("\u9332\u97f3\u307e\u3060\u3057\u3066\u3044\u307e\u305b\u3093\u3002\u9332\u97f3\u30dc\u30bf\u30f3\u3092\u62bc\u3057\u3066\u304f\u3060\u3055\u3044\u3002")
