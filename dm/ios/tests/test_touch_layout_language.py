"""声音页留着原版的语言分节（选项 → 声音 → 文字语言 / 语音语言）：原版自带 13 种语言的串表和语音，我们不能再把入口藏起来
（俄文 = 状态表第 7 个，见原版 SoundOptionsPanelHD.json 的 TextLanguage 轮播）。触屏那份与手柄那份都要留。
The sound page keeps the original game's language section (Options → Sound → Text Language / Voice Language): the original ships string
tables and voice for all 13 languages, so the entry must not be hidden (Russian is state 7 of the TextLanguage carousel in the original
SoundOptionsPanelHD.json). Both the touch copy and the controller copy must keep it.
"""
import sys
from pathlib import Path

root = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(root / 'ios/tools'))
import touch_layout as layout

ROW = '{"type": "TableRowWidget", "name": "Row %s", "children": []}'
src = '{\n  "children": [\n    %s,\n    %s,\n    %s,\n    %s\n  ],\n  "rowHeight": "$OptionsTableRowHeight"\n}\n' % (
    ROW % 'LanguageOptions', ROW % 'VoiceLanguage', ROW % 'TextLanguage', ROW % 'Controller Feedback')

for label, fn, row_pitch in (('touch', layout.PRESENT['soundoptionspanelhd.json'], True), ('controller', layout.PAD_ROOT['soundoptionspanelhd.json'], False)):
    out, n = fn(src)
    for keep in ('Row LanguageOptions', 'Row VoiceLanguage', 'Row TextLanguage'):
        assert '"name": "%s"' % keep in out, (label, keep)
    assert 'Row Controller Feedback' not in out, label
    if row_pitch: assert '"rowHeight": 180' in out, label          # 行距变换照常套上（只在触屏那份） | the row-pitch transform still applies (touch copy only)
print('PASS sound options page keeps the original language section (touch and controller)')
