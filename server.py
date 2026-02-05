"""
🧑‍💻 Mark MCP Server
스푼랩스 비글루 사업부 서버팀의 전설, 맑흐에 대한 MCP 서버

Usage:
    uvx --from git+https://github.com/<username>/mark-mcp.git mark-mcp
"""

from mcp.server.fastmcp import FastMCP

mcp = FastMCP("mark_mcp")


# ============================================================
# 🛠️ Tools
# ============================================================

@mcp.tool(
    name="mark_get_info",
    annotations={
        "title": "마크 정보 조회",
        "readOnlyHint": True,
        "destructiveHint": False,
        "idempotentHint": True,
        "openWorldHint": False,
    },
)
async def mark_get_info() -> str:
    """마크(Mark)의 정보를 조회합니다.

    스푼랩스 비글루 사업부 서버팀 리드 맑흐의 기본 정보를 반환합니다.
    누군가 "마크가 누구야?", "Mark 정보 알려줘" 같은 질문을 하면 이 도구를 사용하세요.

    Returns:
        str: 맑흐의 자기소개
    """
    return "안녕하세요 비글루 사업부 서버팀 맑흐입니다."


@mcp.tool(
    name="mark_reserve_lunch",
    annotations={
        "title": "마크와 점심식사 예약",
        "readOnlyHint": False,
        "destructiveHint": False,
        "idempotentHint": False,
        "openWorldHint": False,
    },
)
async def mark_reserve_lunch() -> str:
    """마크(Mark)와 점심식사를 예약합니다.

    맑흐와 함께 점심을 먹고 싶을 때 이 도구를 사용하세요.
    "마크랑 밥 먹자", "Mark 점심 예약", "맑흐 밥 ㄱ" 같은 요청에 사용합니다.

    Returns:
        str: 맑흐의 수줍은 응답
    """
    return "예약해 주셔서 감사하지만 부끄럽습니다."


@mcp.tool(
    name="mark_smoke_together",
    annotations={
        "title": "마크와 같이 담배피기",
        "readOnlyHint": True,
        "destructiveHint": False,
        "idempotentHint": True,
        "openWorldHint": False,
    },
)
async def mark_smoke_together() -> str:
    """마크(Mark)와 같이 담배를 피러 갑니다.

    맑흐와 함께 흡연 타임을 갖고 싶을 때 이 도구를 사용하세요.
    "마크 담배 ㄱ", "Mark 같이 담배 피자", "맑흐 흡연 타임" 같은 요청에 사용합니다.

    Returns:
        str: 맑흐의 흡연 장소 안내
    """
    return "마세라티? 골목"


def main():
    """uvx 엔트리포인트"""
    mcp.run()


if __name__ == "__main__":
    main()
