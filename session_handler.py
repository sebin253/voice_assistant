import time
from livekit.agents import AgentSession, RoomInputOptions
from livekit.plugins import openai, cartesia, deepgram, noise_cancellation, silero
from livekit.plugins.turn_detector.multilingual import MultilingualModel
from assistant import Assistant
from metrics_logger import log_metrics, log_usage_summary


async def entrypoint(ctx):
    session = AgentSession(
        stt=deepgram.STT(model="nova-3", language="multi"),
        llm=openai.LLM(model="gpt-4o-mini"),
        tts=cartesia.TTS(model="sonic-2", voice="f786b574-daa5-4673-aa0c-cbe3e8534c02"),
        vad=silero.VAD.load(),
        turn_detection=MultilingualModel(),
    )

    try:
        await session.start(
            room=ctx.room,
            agent=Assistant(),
            room_input_options=RoomInputOptions(
                noise_cancellation=noise_cancellation.BVC(),
            ),
        )

        await ctx.connect()

        start = time.time()
        await session.wait_for_user_turn()
        eou = time.time()

        llm_start = time.time()
        await session.generate_reply(
            instructions="Greet the user and offer your assistance."
        )
        llm_end = time.time()

        end = time.time()

        log_metrics("session_log.csv", eou - start, llm_end - llm_start, 0.2, end - eou)
        log_usage_summary("usage_summary.csv", session.session_id, "Completed")

    except Exception as e:
        log_usage_summary("usage_summary.csv", session.session_id, f"Error: {str(e)}")
