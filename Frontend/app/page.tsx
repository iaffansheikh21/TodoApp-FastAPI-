// 'use client'
// import { useState, useEffect } from 'react';
// import axios from 'axios';

// interface Todo {
//   id: number;
//   title: string;
//   description: string;
//   is_completed: boolean;
// }

// const Home = () => {
//   const [todos, setTodos] = useState<Todo[]>([]);
//   const [title, setTitle] = useState('');
//   const [description, setDescription] = useState('');
//   const [isCompleted, setIsCompleted] = useState(false);
//   const [updateId, setUpdateId] = useState<number | null>(null);

//   useEffect(() => {
//     // fetchTodos();
//   }, []);

//   const fetchTodos = async () => {
//     try {
//       const response = await axios.get('http://127.0.0.1:8080/get_todos');
//       setTodos(response.data);
//     } catch (error) {
//       console.error('Error fetching todos:', error);
//     }
//   };

//   const handleCreateTodo = async () => {
//     try {
//       await axios.post('http://127.0.0.1:8080/create_todo', {
//         title,
//         description,
//         is_completed: isCompleted,
//       });
//       fetchTodos();
//       setTitle('');
//       setDescription('');
//       setIsCompleted(false);
//     } catch (error) {
//       console.error('Error creating todo:', error);
//     }
//   };

//   const handleUpdateTodo = async (id: number) => {
//     try {
//       await axios.put(`http://127.0.0.1:8080/update_todo/${id}`, {
//         title,
//         description,
//         is_completed: isCompleted,
//       });
//       fetchTodos();
//       setUpdateId(null);
//       setTitle('');
//       setDescription('');
//       setIsCompleted(false);
//     } catch (error) {
//       console.error('Error updating todo:', error);
//     }
//   };

//   const handleDeleteTodo = async (id: number) => {
//     try {
//       await axios.delete(`http://127.0.0.1:8080/delete_todo/${id}`);
//       fetchTodos();
//     } catch (error) {
//       console.error('Error deleting todo:', error);
//     }
//   };

//   const getAllTodos = () => {
//     fetchTodos();
//   };

//   return (
//     <div className="p-4 max-w-2xl mx-auto">
//       <h1 className="text-2xl font-bold mb-4 text-center">Todo List</h1>

//       <div className="mb-4">
//         <input
//           type="text"
//           placeholder="Title"
//           value={title}
//           onChange={(e) => setTitle(e.target.value)}
//           className="border p-2 mb-2 w-full"
//         />
//         <textarea
//           placeholder="Description"
//           value={description}
//           onChange={(e) => setDescription(e.target.value)}
//           className="border p-2 mb-2 w-full"
//         />
//         <label className="flex items-center mb-2">
//           <input
//             type="checkbox"
//             checked={isCompleted}
//             onChange={(e) => setIsCompleted(e.target.checked)}
//             className="mr-2"
//           />
//           Completed
//         </label>
//         <button
//           onClick={() => (updateId ? handleUpdateTodo(updateId) : handleCreateTodo())}
//           className="bg-blue-500 text-white px-4 py-2 rounded"
//         >
//           {updateId ? 'Update Todo' : 'Add Todo'}
//         </button>
//       </div>

//       <button
//         onClick={getAllTodos}
//         className="bg-green-500 text-white px-4 py-2 rounded mb-4"
//       >
//         Get All Todos
//       </button>

//       <ul>
//         {todos.map((todo) => (
//           <li key={todo.id} className="mb-2 p-2 border border-gray-300 rounded">
//             <h3 className="text-lg font-semibold">{todo.title}</h3>
//             <p>{todo.description}</p>
//             <label className="flex items-center mb-2">
//               <input
//                 type="checkbox"
//                 checked={todo.is_completed}
//                 onChange={() => handleUpdateTodo(todo.id)}
//                 className="mr-2"
//                 disabled
//               />
//               Completed
//             </label>
//             <button
//               onClick={() => {
//                 setUpdateId(todo.id);
//                 setTitle(todo.title);
//                 setDescription(todo.description);
//                 setIsCompleted(todo.is_completed);
//               }}
//               className="bg-yellow-500 text-white px-4 py-2 rounded mr-2"
//             >
//               Edit
//             </button>
//             <button
//               onClick={() => handleDeleteTodo(todo.id)}
//               className="bg-red-500 text-white px-4 py-2 rounded"
//             >
//               Delete
//             </button>
//           </li>
//         ))}
//       </ul>
//     </div>
//   );
// };

// export default Home;


'use client';
import { useState, useEffect } from 'react';
import axios from 'axios';

interface Todo {
  id: number;
  title: string;
  description: string;
  is_completed: boolean;
}

const Home = () => {
  const [todos, setTodos] = useState<Todo[]>([]);
  const [title, setTitle] = useState('');
  const [description, setDescription] = useState('');
  const [isCompleted, setIsCompleted] = useState(false);
  const [updateId, setUpdateId] = useState<number | null>(null);

  // useEffect(() => {
  //   fetchTodos();
  // }, []);

  const fetchTodos = async () => {
    try {
      const response = await axios.get('http://127.0.0.1:8080/get_todos');
      setTodos(response.data);
    } catch (error) {
      console.error('Error fetching todos:', error);
    }
  };

  const handleCreateTodo = async () => {
    try {
      await axios.post('http://127.0.0.1:8080/create_todo', {
        title,
        description,
        is_completed: isCompleted,
      });
      fetchTodos();
      resetForm();
    } catch (error) {
      console.error('Error creating todo:', error);
    }
  };

  const handleUpdateTodo = async (id: number) => {
    try {
      await axios.put(`http://127.0.0.1:8080/update_todo/${id}`, {
        title,
        description,
        is_completed: isCompleted,
      });
      fetchTodos();
      resetForm(); // Reset the form after updating
    } catch (error) {
      console.error('Error updating todo:', error);
    }
  };

  const handleDeleteTodo = async (id: number) => {
    try {
      await axios.delete(`http://127.0.0.1:8080/delete_todo/${id}`);
      fetchTodos();
    } catch (error) {
      console.error('Error deleting todo:', error);
    }
  };

  const resetForm = () => {
    setTitle('');
    setDescription('');
    setIsCompleted(false);
    setUpdateId(null);
  };

  const getAllTodos = () => {
    fetchTodos();
  };

  return (
    <div className="p-4 max-w-2xl mx-auto">
      <h1 className="text-2xl font-bold mb-4 text-center">Todo List</h1>

      <div className="mb-4">
        <input
          type="text"
          placeholder="Title"
          value={title}
          onChange={(e) => setTitle(e.target.value)}
          className="border p-2 mb-2 w-full"
        />
        <textarea
          placeholder="Description"
          value={description}
          onChange={(e) => setDescription(e.target.value)}
          className="border p-2 mb-2 w-full"
        />
        <label className="flex items-center mb-2">
          <input
            type="checkbox"
            checked={isCompleted}
            onChange={(e) => setIsCompleted(e.target.checked)}
            className="mr-2"
          />
          Completed
        </label>
        <button
          onClick={() => (updateId ? handleUpdateTodo(updateId) : handleCreateTodo())}
          className="bg-blue-500 text-white px-4 py-2 rounded"
        >
          {updateId ? 'Update Todo' : 'Add Todo'}
        </button>
        {updateId && (
          <button
            onClick={resetForm}
            className="bg-gray-500 text-white px-4 py-2 rounded ml-2"
          >
            Cancel Edit
          </button>
        )}
      </div>

      <button
        onClick={getAllTodos}
        className="bg-green-500 text-white px-4 py-2 rounded mb-4"
      >
        Get All Todos
      </button>

      <ul>
        {todos.map((todo) => (
          <li key={todo.id} className="mb-2 p-2 border border-gray-300 rounded">
            <h3 className="text-lg font-semibold">{todo.title}</h3>
            <p>{todo.description}</p>
            <label className="flex items-center mb-2">
              <input
                type="checkbox"
                checked={todo.is_completed}
                className="mr-2"
                disabled
              />
              Completed
            </label>
            <button
              onClick={() => {
                setUpdateId(todo.id);
                setTitle(todo.title);
                setDescription(todo.description);
                setIsCompleted(todo.is_completed);
              }}
              className="bg-yellow-500 text-white px-4 py-2 rounded mr-2"
            >
              Edit
            </button>
            <button
              onClick={() => handleDeleteTodo(todo.id)}
              className="bg-red-500 text-white px-4 py-2 rounded"
            >
              Delete
            </button>
          </li>
        ))}
      </ul>
    </div>
  );
};

export default Home;
