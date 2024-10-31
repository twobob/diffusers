from ...utils import is_flax_available, is_torch_available


if is_torch_available():
    from .autoencoder_asym_kl import AsymmetricAutoencoderKL
    from .autoencoder_kl import AutoencoderKL
    from .autoencoder_kl_allegro import AutoencoderKLAllegro
    from .autoencoder_kl_cogvideox import AutoencoderKLCogVideoX
    from .autoencoder_kl_temporal_decoder import AutoencoderKLTemporalDecoder
    from .autoencoder_oobleck import AutoencoderOobleck
    from .autoencoder_tiny import AutoencoderTiny
    from .consistency_decoder_vae import ConsistencyDecoderVAE
    from .vq_model import VQModel


if is_flax_available():
    from .vae_flax import FlaxAutoencoderKL
