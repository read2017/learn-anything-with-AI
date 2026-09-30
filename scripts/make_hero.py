#!/usr/bin/env python3
"""生成 assets/hero.gif —— README 顶部的动图。

内容：learn-anything-skill 的教学闭环
  默认角色 → 诊断起点 → 学习路线 → 项目化练习 → 掌握度检查 → 卡点落盘
后半段切换到 6 条核心特性。图形全部现画，不使用任何人物肖像或第三方素材。

依赖：Pillow
用法：python3 scripts/make_hero.py
"""
import os

from PIL import Image, ImageDraw, ImageFont

RESAMPLE = getattr(Image, "Resampling", Image).LANCZOS

W, H = 1200, 620
FPS = 12
BG = (13, 17, 23)
FG = (234, 240, 246)
DIM = (139, 148, 158)
LINE = (48, 54, 61)
ACC = (88, 166, 255)      # 蓝
ACC2 = (63, 185, 80)      # 绿
ACC3 = (210, 153, 34)     # 黄
ACC4 = (188, 140, 255)    # 紫

FONT_CANDIDATES = [
    "/System/Library/Fonts/STHeiti Medium.ttc",
    "/Library/Fonts/Arial Unicode.ttf",
    "/System/Library/Fonts/Supplemental/Songti.ttc",
]


def pick(cands, size):
    for c in cands:
        if os.path.exists(c):
            try:
                return ImageFont.truetype(c, size)
            except Exception:
                continue
    return ImageFont.load_default()


def ease(t):
    t = max(0.0, min(1.0, t))
    return 1 - (1 - t) ** 3


def layer():
    return Image.new("RGBA", (W, H), BG + (255,))


def blend(col, a):
    return tuple(int(col[i] * a + BG[i] * (1 - a)) for i in range(3))


def draw_centered(d, y, text, font, fill, alpha=1.0):
    if alpha <= 0.01:
        return
    bbox = d.textbbox((0, 0), text, font=font)
    d.text(((W - (bbox[2] - bbox[0])) / 2 - bbox[0], y), text, font=font,
           fill=blend(fill, alpha) + (255,))


def draw_glyph(img, cx, cy, R, alpha=1.0):
    """顶部标记：圆环 + 内部三条递增横线（象征掌握度逐层上升）"""
    if alpha <= 0.01:
        return
    S = 4
    size = R * 2 * S
    canvas = Image.new("RGBA", (size, size), (0, 0, 0, 0))
    cd = ImageDraw.Draw(canvas)
    cd.ellipse([3 * S, 3 * S, size - 3 * S, size - 3 * S],
               outline=blend(ACC, alpha) + (255,), width=2 * S + S // 2)
    gap = size * 0.145
    y0 = size * 0.325
    for i, (frac, col) in enumerate([(0.54, ACC2), (0.74, ACC3), (0.94, ACC4)]):
        w = size * 0.52 * frac
        x0 = (size - w) / 2
        y1 = y0 + i * gap
        cd.rounded_rectangle([x0, y1, x0 + w, y1 + gap * 0.44],
                             radius=gap * 0.22, fill=blend(col, alpha) + (255,))
    canvas = canvas.resize((R * 2, R * 2), RESAMPLE)
    img.paste(canvas, (int(cx - R), int(cy - R)), canvas)


# ---------- 文案 ----------
TITLE = "Learn Anything Skill"
SUBTITLE = "让 AI 从「会回答问题」，变成「能带你真的学会」"

FLOW = [
    ("导师 + 项目教练", "不是问答机器人", ACC),
    ("诊断起点", "先搞清你在哪一层", ACC),
    ("学习路线", "阶段 · 周计划 · 验收标准", ACC),
    ("项目化练习", "真做东西，不是看教程", ACC3),
    ("掌握度检查", "知道→会用→会改→会迁移", ACC2),
    ("卡点落盘", "写成 Markdown 可复盘", ACC2),
]

FEATS = [
    ("①", "项目驱动：每轮都产出一个能拿出手的东西", ACC),
    ("②", "Mastery Learning：没掌握就不往下走", ACC),
    ("③", "中文主讲 · 温柔鼓励 · 专业幽默", ACC3),
    ("④", "没资料时主动补官方文档与权威材料", ACC4),
    ("⑤", "产出落盘成 Markdown，可复盘可交作业", ACC2),
    ("⑥", "一个 SKILL.md 走遍 Codex / Claude Code / OpenCode", ACC2),
]

FOOT_L = "MIT 开源 · npx skills add read2017/learn-anything-with-AI"
FOOT_R = "189 stars · 15 forks · 中文优先 · 适配任意 Agent Skill 客户端"

# 时间轴（秒）
T_FLOW_START = 1.40
T_FLOW_STEP = 0.33
T_SWITCH = 5.05          # 流水线 → 特性
T_FEAT_START = 5.22
T_FEAT_STEP = 0.25
T_FOOT = 6.45
TOTAL = 7.9

# 流水线两列起点
X_DOT = 366
X_KEY = 392
X_VAL = 604
Y_FLOW = 262
ROW_FLOW = 44


def frame(t):
    img = layer()
    d = ImageDraw.Draw(img)
    f_title = pick(FONT_CANDIDATES, 62)
    f_sub = pick(FONT_CANDIDATES, 24)
    f_key = pick(FONT_CANDIDATES, 26)
    f_val = pick(FONT_CANDIDATES, 22)
    f_featmk = pick(FONT_CANDIDATES, 24)
    f_feat = pick(FONT_CANDIDATES, 22)
    f_foot = pick(FONT_CANDIDATES, 18)
    f_small = pick(FONT_CANDIDATES, 16)

    # ── 阶段 1：标记 + 标题 ──
    a1 = ease(t / 0.85)
    draw_glyph(img, W / 2, 80 + int(12 * (1 - a1)), 46, a1)
    draw_centered(d, 138, TITLE, f_title, FG, a1)
    if t > 0.48:
        draw_centered(d, 216, SUBTITLE, f_sub, DIM, ease((t - 0.48) / 0.65))

    # ── 阶段 2：教学闭环 ──
    if t < T_SWITCH:
        for i, (key, val, color) in enumerate(FLOW):
            st = T_FLOW_START + i * T_FLOW_STEP
            if t < st:
                break
            a = ease((t - st) / 0.42)
            if t > T_SWITCH - 0.18:
                a *= max(0.0, 1 - (t - (T_SWITCH - 0.18)) / 0.18)
            y = Y_FLOW + i * ROW_FLOW + int(13 * (1 - a))
            d.ellipse([X_DOT - 4, y + 14, X_DOT + 4, y + 22],
                      fill=blend(color, a) + (255,))
            d.text((X_KEY, y), key, font=f_key, fill=blend(FG, a) + (255,))
            d.text((X_VAL, y + 6), val, font=f_val, fill=blend(DIM, a) + (255,))
    # ── 阶段 3：核心特性 ──
    else:
        a_h = ease((t - T_SWITCH) / 0.38)
        draw_centered(d, 244, "它和「问 ChatGPT 一个问题」的区别",
                      pick(FONT_CANDIDATES, 23), DIM, a_h)
        for i, (mk, text, color) in enumerate(FEATS):
            st = T_FEAT_START + i * T_FEAT_STEP
            if t < st:
                break
            a = ease((t - st) / 0.42)
            y = 286 + i * 40 + int(11 * (1 - a))
            bbox = d.textbbox((0, 0), text, font=f_feat)
            tw = bbox[2] - bbox[0]
            mk_bbox = d.textbbox((0, 0), mk, font=f_featmk)
            mw = mk_bbox[2] - mk_bbox[0]
            total = mw + 14 + tw
            x0 = (W - total) / 2
            d.text((x0 - mk_bbox[0], y), mk, font=f_featmk,
                   fill=blend(color, a) + (255,))
            d.text((x0 + mw + 14 - bbox[0], y + 2), text, font=f_feat,
                   fill=blend(color, a) + (255,))

    # ── 阶段 4：底栏 ──
    if t > T_FOOT:
        a = ease((t - T_FOOT) / 0.5)
        d.line([(110, H - 86), (W - 110, H - 86)],
               fill=blend(LINE, a) + (255,), width=1)
        draw_centered(d, H - 68, FOOT_L, f_foot, ACC2, a)
        draw_centered(d, H - 40, FOOT_R, f_small, DIM, a * 0.95)

    return img.convert("RGB")


def main():
    root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    out = os.path.join(root, "assets", "hero.gif")
    os.makedirs(os.path.dirname(out), exist_ok=True)
    n = int(TOTAL * FPS)
    frames = [frame(i / FPS) for i in range(n)]
    qs = [f.quantize(colors=128) for f in frames]
    qs[0].save(out, save_all=True, append_images=qs[1:],
               duration=int(1000 / FPS), loop=0, optimize=True)
    print(f"✅ {out}")
    print(f"   {n} 帧 · {TOTAL}s · {W}x{H} · {os.path.getsize(out)/1024/1024:.2f} MB")


if __name__ == "__main__":
    main()
