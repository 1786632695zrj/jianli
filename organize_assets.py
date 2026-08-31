import shutil
from pathlib import Path

src = Path("F:/0workbuddy文件存放/2026-08-31-00-02-43/portfolio_assets")
dst = Path("F:/0workbuddy文件存放/2026-08-31-00-02-43/assets")
dst.mkdir(exist_ok=True)

files_to_copy = {
    # portraits
    "../../Desktop/我的资料/生活图片.jpg": "portrait.jpg",
    # school logos
    "ppt_images/ppt_image_023.png": "swust_logo.png",
    "ppt_images/ppt_image_034.jpeg": "chd_logo.jpeg",
    # dashboards
    "ppt_images/ppt_image_003.png": "db_dabao.png",
    "ppt_images/ppt_image_059.png": "db_store.png",
    "ppt_images/ppt_image_058.png": "db_taoke.png",
    "ppt_images/ppt_image_004.png": "db_guobu.png",
    "ppt_images/ppt_image_005.png": "db_toufang.png",
    "ppt_images/ppt_image_006.png": "db_live.png",
    "ppt_images/ppt_image_002.png": "db_pinxiao.png",
    # AI plugin
    "ppt_images/ppt_image_032.png": "ai_plugin.png",
    "ppt_images/ppt_image_037.jpeg": "ai_databank.jpeg",
    "ppt_images/ppt_image_040.png": "ai_report_yoga.png",
    "ppt_images/ppt_image_043.png": "ai_knowledge_base.png",
    # AB test / creative
    "ppt_images/ppt_image_026.png": "ab_matrix.png",
    "ppt_images/ppt_image_024.png": "ab_fuxi.png",
    "ppt_images/ppt_image_011.png": "ab_steps.png",
    # product posters
    "ppt_images/ppt_image_017.jpeg": "y900.jpeg",
    "ppt_images/ppt_image_021.png": "xiaoxin_air13.png",
    "ppt_images/ppt_image_019.png": "lecoo_air14.png",
    # lenovo activities
    "ppt_images/ppt_image_047.jpeg": "lenovo_store1.jpeg",
    "ppt_images/ppt_image_048.jpeg": "lenovo_store2.jpeg",
    "ppt_images/ppt_image_052.jpeg": "future_center.jpeg",
    "ppt_images/ppt_image_053.jpeg": "campus_ambassador.jpeg",
    "ppt_images/ppt_image_051.jpeg": "ai_camp.jpeg",
    # portfolio pages
    "portfolio_pages/page_03.png": "portfolio_1.png",
    "portfolio_pages/page_04.png": "portfolio_2.png",
    "portfolio_pages/page_05.png": "portfolio_3.png",
    "portfolio_pages/page_06.png": "portfolio_4.png",
    "portfolio_pages/page_07.png": "portfolio_5.png",
    "portfolio_pages/page_08.png": "portfolio_6.png",
}

for src_rel, name in files_to_copy.items():
    s = src / src_rel if not src_rel.startswith("..") else Path("C:/Users/DELL" + src_rel[5:])
    if s.exists():
        shutil.copy2(s, dst / name)
        print(f"Copied {s.name} -> {name}")
    else:
        print(f"Missing: {s}")

# Copy video
video_src = src / "ppt_video_001.mp4"
if video_src.exists():
    shutil.copy2(video_src, dst / "plugin_demo.mp4")
    print("Copied plugin demo video")

print("Done.")
