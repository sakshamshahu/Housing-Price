import { Route, Routes } from 'react-router-dom'
import './App.css'
import Navbar from './components/Navbar'
import Prediction from './pages/Prediction'
import NotFound from './pages/NotFound'
import Home from './pages/Home'

function App() {


  return (

    <div className=' h-[100vh] w-[100vw] bg-darkBlue text-white overflow-hidden'>

      <div className=' w-10/12 mx-auto'>

          <Navbar/>

      </div>


      <Routes>
        <Route path='/' element={ <Home/> }></Route>
        <Route path='/predict' element={ <Prediction/> }></Route>
        <Route path='*' element={ <NotFound/> }></Route>
      </Routes>

    </div>

  )
}

export default App
