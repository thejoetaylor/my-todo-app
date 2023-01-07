import streamlit as st
import functions

if "new_todo" not in st.session_state:
    st.session_state.new_todo = ""

count = 0
todos = functions.get_todos()


def add_todo():
    todo = st.session_state["new_todo"] + "\n"
    todos.append(todo)
    functions.write_todos(todos)


st.title("My Todo App")
st.subheader("This is my Todo App")
st.write("This app is to increase your productivity")


for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=count)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
#       del st.session_state[todo]
        st.experimental_rerun()
    count = count + 1


st.text_input(label="Please add a todo:", placeholder="Add new todo...",
              on_change=add_todo, key="new_todo")
