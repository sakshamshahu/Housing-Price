import React from 'react'
import { useNavigate } from 'react-router-dom'

function Navbar() {

  const navi = useNavigate()
  function logoClickHandler(){
    navi('/')
  }

  return (
    <div>

        <nav className=' text-white flex justify-between items-baseline py-5 align-b'>

            <div className=' text-4xl font-bold cursor-pointer' onClick={logoClickHandler}>Predictor.io</div>

            <div className='flex gap-5 text-2xl'>
                <div>about</div>
                <div>contact</div>
            </div>

        </nav>

    </div>
  )
}

export default Navbar