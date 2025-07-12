from beam import endpoint, env, Output, Image

if env.is_remote():
    from f5_tts.api import F5TTS
    import soundfile as sf
    from utils import clean_text


image = (
    Image(
        base_image="nvidia/cuda:12.4.1-devel-ubuntu22.04",
        python_version="python3.10",
        python_packages=[
            "torch==2.4.0",
            "torchaudio==2.4.0"
        ]
    )
    .add_commands(
        [
            "git clone https://github.com/SWivid/F5-TTS.git /f5-tts",
            "cd /f5-tts && pip install -e .",
            # "pip install git+https://github.com/CodeLinkIO/Vietnamese-text-normalization.git@main"
        ]
    )
    .add_commands([
        "pip install git+https://github.com/CodeLinkIO/Vietnamese-text-normalization.git@main",
        "pip install viet_number",
    ])
)


def load_model():


    model = F5TTS(
        vocab_file="ckpts/trainned/vocab.txt",
        ckpt_file="ckpts/trainned/model_1307000.pt",
        model="F5TTS_v1_Base",
    )

    return model

@endpoint(
    image=image,
    name="f5_tts",
    cpu=2,
    memory="32Gi",
    gpu="A10G",
    on_start=load_model,
)
def generate_speech(context, **inputs):
    model = context
    return {"msg" : "Ok"}