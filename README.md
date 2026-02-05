# 🧑‍💻 Mark MCP Server

> 스푼랩스 비글루 사업부 서버팀의 전설, **맑흐**에 대한 MCP 서버

## 🛠️ 제공 도구

| 도구 | 설명 | 응답 |
|------|------|------|
| `mark_get_info` | 마크 정보 조회 | "안녕하세요 비글루 사업부 서버팀 맑흐입니다." |
| `mark_reserve_lunch` | 마크와 점심식사 예약 | "예약해 주셔서 감사하지만 부끄럽습니다." |
| `mark_smoke_together` | 마크와 같이 담배피기 | "마세라티? 골목" |

## 🚀 uvx로 바로 실행

```bash
uvx --from git+https://github.com/<username>/mark-mcp.git mark-mcp
```

## ⚙️ Claude Desktop 연동

`claude_desktop_config.json`:

```json
{
  "mcpServers": {
    "mark_mcp": {
      "command": "uvx",
      "args": ["--from", "git+https://github.com/<username>/mark-mcp.git", "mark-mcp"]
    }
  }
}
```

> **Config 파일 위치**
> - macOS: `~/Library/Application Support/Claude/claude_desktop_config.json`
> - Windows: `%APPDATA%\Claude\claude_desktop_config.json`

## ⚙️ Claude Code 연동

```bash
claude mcp add mark_mcp -- uvx --from git+https://github.com/<username>/mark-mcp.git mark-mcp
```

## 📦 Git 배포 방법

```bash
cd mark-mcp
git init
git add .
git commit -m "🧑‍💻 맑흐 MCP 서버 초기 커밋"
git remote add origin https://github.com/<username>/mark-mcp.git
git push -u origin main
```

push 하고 나면 누구든 `uvx` 한 줄로 설치 없이 바로 실행할 수 있습니다!

## 💡 사용 예시

Claude에게 이렇게 말해보세요:

- "마크가 누구야?"
- "맑흐랑 점심 먹고 싶어"
- "마크 담배 ㄱ"
