<p align="center"><img src="docs/banner.png" alt="TTS 끝소리 고치기: AI 목소리가 말하다 만 것처럼 끊길 때" width="100%"></p>

<p align="center">
<a href="https://github.com/reedodev/tts-tail-fix/actions/workflows/test.yml"><img src="https://github.com/reedodev/tts-tail-fix/actions/workflows/test.yml/badge.svg" alt="test"></a>
<img src="https://img.shields.io/badge/Claude_Code-skill-2547F4" alt="Claude Code skill">
<img src="https://img.shields.io/badge/license-MIT-black" alt="MIT">
</p>

# TTS 끝소리 고치기 (tts-tail-fix)

보이스 클론 TTS의 마지막 음절이 뚝 끊기는 문제를 찾아내고, 문장 끝에 버리는 단어를 붙여 합성한 뒤 쉼에서 자르는 방법과 실제 소리 끝의 페이드로 고칩니다. 효과가 없었던 방법도 함께 적었습니다.

<!-- prereq-adapt -->
## 무엇이 필요한가요?

꼭 필요한 것은 Python 3.10 이상과 `pip install numpy soundfile`, TTS로 만든 음성 파일(wav, flac)입니다. 권장·선택 준비물까지 정리한 표는 [SKILL.md의 준비물](skills/tts-tail-fix/SKILL.md#준비물-쓰기-전에-있어야-하는-것)에 있습니다.

## 바꿔 쓰기

에이전트에게 다음처럼 말하면 옵션을 바꿔서 실행합니다.

- "영어 음성이야" → 센티널을 ` okay.`처럼 그 언어의 짧은 말로 바꿉니다. 나머지 절차는 같습니다
- "숨소리가 커서 쉼을 못 찾아" → `--silence-db -45` (조용하다고 볼 기준을 올립니다)
- "쉼이 짧은 목소리야" → `--min-pause 0.15`

말과 옵션의 대응표는 [SKILL.md의 바꿔 쓰기](skills/tts-tail-fix/SKILL.md#바꿔-쓰기-이렇게-말하세요)에 있습니다.

## 설치

**Claude Code 플러그인으로 설치**

```
/plugin marketplace add reedodev/tts-tail-fix
/plugin install tts-tail-fix@tts-tail-fix
```

**폴더만 복사**

```bash
git clone https://github.com/reedodev/tts-tail-fix.git
cp -r tts-tail-fix/skills/tts-tail-fix ~/.claude/skills/
```

필요한 것: Python 3.10+, numpy, soundfile

## 바로 해 보기

```bash
pip install numpy soundfile
python skills/tts-tail-fix/scripts/tts_tail.py check narration.wav
python skills/tts-tail-fix/scripts/tts_tail.py cut raw_with_sentinel.wav clean.wav
```

자세한 절차, 옵션, 한계는 [SKILL.md](skills/tts-tail-fix/SKILL.md)에 있습니다. 에이전트가 이 파일을 읽고 그대로 따릅니다.

## 시험

`node tests/run.mjs`가 SKILL.md 형식을 검사하고 예시 파일로 스크립트를 실제로 실행합니다. 푸시할 때마다 GitHub Actions가 같은 시험을 돌립니다(위 test 배지).

## 만든 사람

**리도**, AI 좌충우돌 실습 중인 20년차 엔지니어입니다. 매일 AI에게 일을 맡기다가 막힌 부분을 고쳐 가며 이 스킬을 만들었습니다.
[YouTube @Reedodev](https://www.youtube.com/@Reedodev) · [Threads @reedo.dev](https://www.threads.com/@reedo.dev) · [GitHub @reedodev](https://github.com/reedodev)

같이 만든 다른 스킬: [옵시디언 3D 지식그래프](https://github.com/reedodev/obsidian-brain-3d) · [노트 먼저 찾아보기](https://github.com/reedodev/vault-recall) · [작업 기록 강의자료](https://github.com/reedodev/work-to-lecture-deck) · [한국어 말투 점검](https://github.com/reedodev/korean-tone-check) · [네이버 황금키워드](https://github.com/reedodev/naver-golden-keywords) · [한글 양식 채우기](https://github.com/reedodev/hwpx-form-fill) · [카드뉴스 렌더](https://github.com/reedodev/html-card-render) · [영상 비율 검사](https://github.com/reedodev/social-video-gate) · [유튜브 게시 점검](https://github.com/reedodev/youtube-publish-checklist)

---

## English

Detect and fix TTS / voice-clone clips whose last syllable is chopped off: sentinel word, cut at the pause, fade where the sound really ends, and verify.

Install: `/plugin marketplace add reedodev/tts-tail-fix` then `/plugin install tts-tail-fix@tts-tail-fix`, or copy `skills/tts-tail-fix` into `~/.claude/skills/`. See [SKILL.md](skills/tts-tail-fix/SKILL.md) for the full procedure. MIT License; third-party models, fonts and libraries keep their own licenses.
