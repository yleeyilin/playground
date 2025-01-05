import React from 'react'

function TodoItem({task, deleteTask, toggleCompleted}) {
    function handleChange() {
        toggleCompleted(task.id); 
    }

    return (
        <div className='todo-item'>
            <input
            type='checkbox'
            checked={task.completed}
            onChange={handleChange}
            aria-label={`Mark ${task.text} as ${task.completed ? 'incomplete' : 'complete'}`}
            />
            <p
                style={{
                    textDecoration: task.completed ? 'line-through' : 'none',
                    color: task.completed ? '#888' : '#000',
                }}
            >{task.text}</p>
            <button onClick={() => deleteTask(task.id)}>
                X
            </button>
        </div>
    );
}
export default TodoItem