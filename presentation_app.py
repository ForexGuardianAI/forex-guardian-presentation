import json
from pathlib import Path

import streamlit as st

st.set_page_config(
    page_title="Forex Guardian AI Academy",
    page_icon="🎓",
    layout="wide",
)

st.title("🎓 Forex Guardian AI Academy")
st.caption("Educational Preview | Forex & Futures Learning")

st.info(
    "Welcome to the Forex Guardian AI Academy preview. "
    "This demonstration does not require student login."
)

catalog_path = Path(__file__).parent / "guardian_curriculum_catalog.json"

try:
    with catalog_path.open(encoding="utf-8") as file:
        catalog = json.load(file)
except (OSError, ValueError):
    st.error("The Academy curriculum could not be loaded.")
    st.stop()

modules = catalog.get("modules", [])

st.subheader("Explore the Academy Curriculum")

if isinstance(modules, list) and modules:
    st.write(f"Available learning modules: {len(modules)}")
    for index, module in enumerate(modules, start=1):
        if not isinstance(module, dict):
            continue
        title = str(module.get("title") or f"Module {index}")
        with st.expander(title):
            st.write(module.get("description") or "Explore this learning module.")
            lessons = module.get("lessons", [])
            if isinstance(lessons, list):
                for lesson in lessons:
                    if isinstance(lesson, dict):
                        st.write("•", lesson.get("title", "Lesson"))
else:
    st.warning("No modules are available in this preview.")

st.divider()
st.caption(
    "Educational purposes only. No live trading, "
    "broker connections, or investment advice."
)
