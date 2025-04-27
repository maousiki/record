import streamlit as st
import numpy as np
import soundfile as sf
import tempfile
from st_audiorec import st_audiorec

st.title("🎤 録音ダウンロード専用アプリ (scipy不使用版)")

st.write("👉 録音ボタンを押して音声を録り、WAVファイルにします！")

# 録音ウィジェット
wav_audio_data = st_audiorec()

if isinstance(wav_audio_data, np.ndarray):
    st.success("録音完了！ダウンロードできます！")

    # 一時ファイルに録音を保存 (soundfile使用)
    with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as tmp_wav:
        sf.write(tmp_wav.name, wav_audio_data, samplerate=44100)
        audio_file_path = tmp_wav.name

    # ダウンロードボタン
    with open(audio_file_path, "rb") as f:
        st.download_button(
            label="📥 録音データダウンロード",
            data=f,
            file_name="recorded_audio.wav",
            mime="audio/wav"
        )
else:
    st.info("録音まだしていません。録音ボタンを押してください。")
