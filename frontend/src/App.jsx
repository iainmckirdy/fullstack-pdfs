import { useState } from 'react'
import './css/App.css'
import FileUPload from './components/FileUpload'
import Navbar from './components/NavBar'

function App() {

  return (
    <>
      <Navbar />
      <FileUPload />
    </>
  )
}

export default App
