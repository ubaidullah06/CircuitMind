import sys
import os
import json
import streamlit as st

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from generate.generate import generate_circuit
from explain.explain_module import explain_circuit
from diagnose.diagnose_module import diagnose_circuit
from export.export_module import export_module

st.set_page_config(page_title="CircuitMind", layout="wide")
st.title("⚡ CircuitMind")
st.subheader("AI-Powered Electronics Assistant")

tab1, tab2, tab3, tab4 = st.tabs(["Generate", "Explain", "Diagnose", "Export"])

with tab1:
    st.subheader("Generate New Circuit")
    prompt = st.text_input("Describe your circuit", "make me a LED circuit")
    if st.button("Generate"):
        with st.spinner("Generating..."):
            result = generate_circuit(prompt)
            st.json(result)

with tab2:
    st.subheader("Explain Circuit")
    json_input = st.text_area("Paste circuit JSON", height=250, key="explain")
    if st.button("Explain"):
        try:
            data = json.loads(json_input)
            # Handle both {"circuit_json": {...}} and direct {...}
            if isinstance(data, dict) and "circuit_json" in data:
                data = data["circuit_json"]
            result = explain_circuit(data)
            st.success("**Explanation:**")
            st.write(result.get("explanation", "No explanation"))
            if result.get("warnings"):
                st.warning(str(result["warnings"]))
        except Exception as e:
            st.error(f"Invalid JSON: {e}")

with tab3:
    st.subheader("Diagnose Circuit")
    json_input2 = st.text_area("Paste circuit JSON", height=200, key="diag")
    if st.button("Diagnose"):
        try:
            data = json.loads(json_input2)
            if isinstance(data, dict) and "circuit_json" in data:
                data = data["circuit_json"]
            result = diagnose_circuit(data)
            if result["passed"]:
                st.success("✅ No issues found!")
            else:
                for issue in result["issues"]:
                    st.error(issue)
        except Exception as e:
            st.error(f"Invalid JSON: {e}")

with tab4:
    st.subheader("Export Circuit")
    json_input3 = st.text_area("Paste circuit JSON", height=200, key="export_area")
    fmt = st.selectbox("Format", ["spice", "svg"])
    
    if st.button("Export"):
        try:
            data = json.loads(json_input3)
            if isinstance(data, dict) and "circuit_json" in data:
                data = data["circuit_json"]
            
            result = export_module(json.dumps(data), export_format=fmt, save_to_file=True)
            
            st.json(result)
            
            if fmt == "svg" and "svg_file" in result:
                try:
                    with open(result["svg_file"], "rb") as f:
                        st.download_button(
                            label="📥 Download SVG File",
                            data=f,
                            file_name=result["svg_file"],
                            mime="image/svg+xml"
                        )
                except:
                    st.info("SVG file generated. Check folder.")
                    
            elif fmt == "spice":
                st.download_button(
                    label="📥 Download SPICE File",
                    data=result.get("spice_netlist", ""),
                    file_name="circuit.sp",
                    mime="text/plain"
                )
        except Exception as e:
            st.error(f"Error: {e}")

st.caption("CircuitMind Project")