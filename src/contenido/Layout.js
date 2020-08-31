import React from 'react'
import '../estilo/style.css'
import Prueba from './Prueba'
import Home from './Home'
import Contactanos from './Contactanos'
import {Route, BrowserRouter as Router, Link} from 'react-router-dom'
class Layout extends React.Component{
    render(){
        return(

            <Router>
                
                <div style={{height: '15%', width: '100%', backgroundColor: '#018acc'}}>
                        <img style={{height: '90%', width: '10%', marginTop: '0.5%', marginLeft: '5%', borderRadius: '10px'}} src='https://scontent-mia3-2.xx.fbcdn.net/v/t1.0-9/83970114_1900671686731220_1765311045615747072_n.jpg?_nc_cat=109&_nc_sid=09cbfe&_nc_ohc=Nptr6hJ7sRoAX8mocxn&_nc_ht=scontent-mia3-2.xx&oh=9e19e305ff18d59bef2120577601b44c&oe=5F5EC55A' />
                </div>
                <div style={{height: '5%', width: "100%", backgroundColor: '#07a6f3'}}>
                    <div className="nav">
                        <Link className="active" to='/'>
                            HOME
                        </Link>
                        <Link to='/'>
                        SERVICIOS
                        </Link>
                        <Link to='/prueba-depresion'>
                        PRUEBAS
                        </Link>
                        <Link to='/Contactanos'>
                        CONTACTANOS
                        </Link>
                    </div>
                </div>
                <div>
                    <Route path='/' exact render={(props) => <Home {...props}/>} />
                    <Route path='/prueba-depresion' exact render={(props) => <Prueba {...props}/>} />
                    <Route path='/Contactanos' exact render={(props) => <Contactanos {...props}/>} />
                </div>
            </Router>
        )
    }
}
export default Layout