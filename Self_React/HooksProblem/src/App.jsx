import React, { use, useEffect, useState } from "react";


export default function App() {

  let [count, setCount] = useState(0);
  let [time, setTime] = useState(new Date().toLocaleTimeString());
  let [show, setShow] = useState(true);


  function IncreaseCount() {
    count++;
    setCount(count);

  }
  function DecreaseCount() {
    count--;
    setCount(count);
  }

  useEffect(() => {

    if(!show){
      return;
    }

    const interbalId = setInterval(() => {
      setTime(new Date().toLocaleTimeString());
      console.log("hii")
    }, 1000)

    return () => {
      clearInterval(interbalId)
    }
  }, [show])

  return (
    <>
      <h1 className="bg-black text-white text-2xl font-bold items-center text-center">Hooks UnderStanding</h1>
      <div className="h-dvh max-w-full bg-black font-bold flex justify-center flex-col items-center gap-5 justify-items-center ">
        <p className="text-white font-bold">Count : {count}</p>
        <button onClick={IncreaseCount} className="bg-green-400 rounded-xl p-2 border-white border-3">Increment {count}</button>
        <button onClick={DecreaseCount} className="bg-green-400 rounded-xl p-2 border-white border-3">Decrease {count}</button>
      </div>

      <div className="h-100 bg-black text-white font-extrabold text-3xl flex justify-items-center items-center flex-col">
        <h1>Show Current Time</h1>
        {
          show && <p className="text-7xl">{time}</p>
        }
        <button onClick={() => setShow(!show)} className="border-4 border-green-700 rounded-xl py-2 px-2 mt-6 bg-green-600 hover:bg-green-900">{show?"Show Time":"Hide Time"}</button>
      </div>

    </>
  )
};