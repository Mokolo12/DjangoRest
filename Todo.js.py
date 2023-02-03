  return (
    <li>
      <h3>
        <input defaultChecked={todo.active}
          disabled={true} type="checkbox" />{" "}
        {capitalText}
      </h3>
    </li>
	@@ -19,8 +17,8 @@ const TodoItem = ({ todo }) => {
const TodoList = ({ todoSet }) => {
  return (
    <ul>
      {todoSet.map((todo, index) => (
        <TodoItem key={index} todo={todo} />
      ))}
    </ul>
  );