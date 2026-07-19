// const { createElement } = require("react");

// const ReactDOM = {
//     createRoot: function(container){
//         return {
//             render: function(reactElement){
//                 // Convert Virtual DOM to Real DOM
//                 const element = document.createElement(reactElement.type);

//                 for(const key in reactElement.props){
//                     if(key === 'style'){
//                         Object.assign(element.style, reactElement.props.style);
//                     }
//                     else if(key === 'children'){
//                         element.textContent = reactElement.props[key];
//                     }
//                     else {
//                         element[key] = reactElement.props[key];
//                     }
//                 }

//                 container.appendChild(element);
//             }
//         };
//     }
// };


// const ReactDom = {
//         render : function(element, root){
//                 root.appendChild(element);
//         }
// }


// const element = React.createElement('h1', {
//         style:{
//                 color: "red"
//         }
//      }, 
//        <h1>hello guy's</h1>
// );



const element = <h1>Hello how are you</h1>;

const App = function App(){
        const arr = ["HTML", "CSS", "JAVASCRIPT", "PYTHON"];
      return (
        <>
            <ul>
                {arr.map(arr =>  <li>{arr}</li>)}
            </ul>
        </>
      )
}

const root = ReactDOM.createRoot(document.getElementById('root'));


root.render(<App/>)