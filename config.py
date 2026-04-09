import os

class Config:
    PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))

    # Inference configuration
    # MODEL_PATH = os.path.join(PROJECT_ROOT, "weights", "v1.sim.onnx")
    MODEL_PATH = os.path.join(PROJECT_ROOT, "weights", "v2.onnx")
    TARGET_CLASS_IDS = [1]
    # CAMERA_SOURCE = "https://motchallenge.net/sequenceVideos/PETS09-S2L2-raw.webm"
    CAMERA_SOURCE = "https://rr4---sn-npoe7ney.googlevideo.com/videoplayback?expire=1775769100&ei=rMHXaef8D6Dx4dUP3fmgsQQ&ip=181.228.104.248&id=o-AHUq2sJKU4LykcxaaHuzQ3WZJldZ3_pEj-K-Hrd9e0PQ&itag=137&source=youtube&requiressl=yes&xpc=EgVo2aDSNQ%3D%3D&cps=188&bui=AUUZDGKpyPNTnsNhWpAwNOEmHFxgHXpzwAt7hKWYcCmSCxiv2NEnaohsxxiv9GgsTl4iaCij2FvkcxEr&vprv=1&svpuc=1&mime=video%2Fmp4&rqh=1&gir=yes&clen=5397555538&dur=10795.000&lmt=1773608718777692&keepalive=yes&fexp=51565116,51565682&c=ANDROID_VR&txp=5309224&sparams=expire%2Cei%2Cip%2Cid%2Citag%2Csource%2Crequiressl%2Cxpc%2Cbui%2Cvprv%2Csvpuc%2Cmime%2Crqh%2Cgir%2Cclen%2Cdur%2Clmt&sig=AHEqNM4wRAIgfvHwjOtPICpdeOt4MHpv75mHVIBCtCljsK_WYs_UNxICIBTvOS3jDy92RKADEuaMg7N7ksMgLAbFDvBPoPGQgvH2&rm=sn-uxaxjvh5gbxoupo5-jo9l7k,sn-j5cax8pnpvo-x1xls7d,sn-x1xdd7e&rrc=79,79,104,191&req_id=ee57a08a6ad0a3ee&rms=nxu,au&ipbypass=yes&redirect_counter=4&cm2rm=sn-npoz77z&cms_redirect=yes&cmsv=e&met=1775747524,&mh=uN&mip=139.228.33.9&mm=34&mn=sn-npoe7ney&ms=ltu&mt=1775747095&mv=m&mvi=4&pl=20&lsparams=cps,ipbypass,met,mh,mip,mm,mn,ms,mv,mvi,pl,rms&lsig=APaTxxMwRAIgcNp-jUEcsCm-aZ-_qYFdRG9wpvmRz3xiRvBwlQr-RgACIHFDQc73X3CJRCcGVlTcQcRBXK1WhIJnAzotULAzx0p0"
    YT_LIVESTREAM = False
    DISPLAY_WIDTH = 1024
    DISPLAY_HEIGHT = 576

    # INFERENCE_SIZE = (384, 384) # for v1.sim.onnx model
    INFERENCE_SIZE = (672, 672) # for v2.onnx model
    CONFIDENCE_THRESHOLD = 0.05
    ACTIVATE_TRACKER = False
    TRACKER = "OC-SORT"