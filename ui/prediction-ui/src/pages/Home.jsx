import React from 'react'
import notifications from '../assets/notifications.svg'
import graph from '../assets/graph.svg'
import laptop from '..//assets/laptop.svg'
import person from '../assets/person.svg'
import { useNavigate } from 'react-router-dom'


function Home() {

    const navi = useNavigate()
    function startedHandler(){
        navi('/predict')
    }

  return (
    <div className=' mx-auto w-10/12 flex relative'>

        <div>
            <img src={person} className=' absolute left-[280px] top-[150px] size-[80%] '></img>
        </div>

        {/* left section */}
        <div className=' flex flex-col '>

            <div className=' font-bold text-[5rem] pt-[100px]'> house price</div>

            <div className=' font-bold text-[6.2rem] text-blue-500'> PREDICTION</div>

            <div>
                <button onClick={startedHandler} className=' text-[1.1rem] bg-blue-900 px-3 py-2 rounded-md text-white hover:bg-blue-500 hover:shadow-md hover:shadow-white transition-all duration-300'>GET STARTED</button>
            </div>

            <div>
                <img src={graph} width={400}  className=''></img>
            </div>


        </div>


        {/* right section */}
        <div className=' pl-[300px]'>

            <div>
                <img src={laptop} className=''></img>
            </div>

            <div>
                <img src={notifications}></img>
            </div>

        </div>


    </div>
  )
}

export default Home