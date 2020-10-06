import React from 'react'
import Clinica from '../estilo/images/clinica.jpg'
import Reloj from '../estilo/images/reloj.png'
import Location from '../estilo/images/location.png'
import Llamada from '../estilo/images/llamada.png'
import Mail from '../estilo/images/mail.png'

class Contactanos extends React.Component{
    render(){
        return(              
            <div className='contactp'>
                <div className='Gridcont'>
                    <div style={{height: '100%', width: '75%'}}>
                        <img className='contlo' style={{height: '40%', width: '100%', marginTop: '70%', marginLeft: '1%'}} src={Clinica} />
                    </div>
                    <div>
                        <div className='lemac' style={{marginTop: '4%', marginLeft: '25%', fontSize: '28px', textAlign: 'justify', color:'#016495'}}>
                            <p className='lemac1' style={{marginLeft: '10%'}}>Clinica Humanamente</p>
                            <p>“Bienestar y confianza humanamente”</p>
                        </div>

                        <div className='Gridcont2' style={{fontSize: '19px', fontWeight: 'bold'}}>
                            <img src={Llamada} className='img1' />
                            <div>
                                <p>(502) 2369-3238</p>
                                <p>(502) 2369-0709</p>
                                <p>(502) 2221-7449</p>
                            </div>
                            <img src={Mail} className='img2'/>
                            <p>informacion@clinicahumanamente.com</p>
                            <img src={Location} className='img2'/>
                            <p>Visitenos en: 20 av "A" 0-49 zona 15 Vista Hermosa II</p>
                            <img src={Reloj} className='img1'/>
                            <div>
                                <p>Horario entre semana:</p>
                                <p>Lunes a viernes 8:00 AM - 5:00 PM</p>
                                <p>Sabado 8:00 AM - 12:00 PM</p>
                                <p>Domingo - CERRADO</p>
                            </div>
                        </div>
                    </div>
                </div>   

            </div>

        )
    }
}
export default Contactanos