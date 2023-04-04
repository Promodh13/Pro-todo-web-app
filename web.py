import streamlit as st
import function

todos = function.get_todos()



def add_todo():
    todo = st.session_state["new_todo"] + '\n'
    todos.append(todo)
    function.write_todos(todos)


st.title("Pro's Todo App")

st.subheader("This is my todo app.")

st.write("This app is to increase your productivity.")

for index, todo in enumerate(todos):
    check_box = st.checkbox(todo, key=todo)
    if check_box:
        todos.pop(index)
        function.write_todos(todos)
        del st.session_state[todo]
        st.experimental_rerun()

st.text_input(label="Add a todo:", placeholder="Add a new todo...",
              label_visibility="hidden",
              on_change=add_todo, key="new_todo")