import React from 'react'
import Clinica from '../estilo/images/clinica.jpg'

class Home extends React.Component{
    render(){
        return(              
        <div className='homep'>
            <div className='Gridh'>
                <div style={{height: '100%', width: '75%'}}>
                    <img className='logoi' src={Clinica} />
                </div>
                <div>
                    <div className='lema'>
                        <p>“Bienestar y confianza humanamente”</p>
                    </div>
                    <div style={{width: '95%', fontSize: '28px', textAlign: 'justify'}}>
                        <p>La clínica de servicios exclusivos de salud mental más grande de Centroamérica, que reúne a 12 psiquiatras y 9 psicólogas, con experiencia en investigación, docencia universitaria y práctica clínica.</p>
                    </div>
                </div>
            </div>   
            <div className='intro'>
                <p>La mayoría de nuestros miembros cuenta con entrenamientos y certificaciones profesionales internacionales. Desde su fundación hace 11 años; se ha caracterizado por innovar en tratamientos basados en la evidencia, especializarse en el tratamiento de enfermedades afectivas resistentes, así como en la formación y certificación de profesionales de la salud mental.</p>
                <p>También en áreas complementarias al tratamiento psicoterapéutico y psicofarmacológico, como farmacia especializada, pruebas de evaluación, talleres individuales y de pareja para clientes, laboratorio del sueño portátil y clínica de neuroestimulación.</p>
                <p>Estamos comprometidos para formar un equipo de trabajo de acorde a las necesidades individuales de los clientes y sus familias que requieran asistencia de salud mental, utilizando los tratamientos más eficaces, siempre buscando alcanzar el bienestar y confianza de quiénes nos visitan.</p>
            </div>

         </div>

        )
    }
}
export default Home