import streamlit as st

st.title("Student Grade Application")
st.header("Enter your mark to find the grade.")

mark = st.number_input("Enter your mark (0-100): ")

if st.button("Calculate Grade"):
    if (mark < 0) | (mark > 100):
        st.error("Please enter a valid mark between 0 and 100.")
        grade = "Invalid"
    else:
        if mark >= 90:
            grade = "A"
        elif mark >= 80:
            grade = "B"
        elif mark >= 70:
            grade = "C"
        elif mark >= 60:
            grade = "D"
        else:
            grade = "E"
    
    if grade == "A":
        st.success(f"Mark {mark} Grade: {grade}")
    elif grade == "B":
        st.info(f"Mark {mark} Grade: {grade}")
    elif (grade == "C") | (grade == "D"):
        st.warning(f"Mark {mark} Grade: {grade}")
    elif grade == "E":
        st.error(f"Mark {mark} Grade: {grade}")