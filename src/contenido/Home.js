import React from 'react'

class Home extends React.Component{
    render(){
        return(              
        <div>
            <div className='Gridh'>
                <div style={{height: '100%', width: '75%'}}>
                    <img style={{height: '95%', width: '100%', marginTop: '0.5%', marginLeft: '15%'}} src='https://scontent-mia3-2.xx.fbcdn.net/v/t1.0-9/83970114_1900671686731220_1765311045615747072_n.jpg?_nc_cat=109&_nc_sid=09cbfe&_nc_ohc=Nptr6hJ7sRoAX8mocxn&_nc_ht=scontent-mia3-2.xx&oh=9e19e305ff18d59bef2120577601b44c&oe=5F5EC55A' />
                </div>
                <div>
                    <div style={{marginTop: '4%', marginLeft: '25%', fontSize: '28px', textAlign: 'justify', color:'#016495'}}>
                        <p>“Bienestar y confianza humanamente”</p>
                        </div>


                        <div style={{width: '95%', fontSize: '28px', textAlign: 'justify'}}>
                        <p>La clínica de servicios exclusivos de salud mental más grande de Centroamérica, que reúne a 12 psiquiatras y 9 psicólogas, con experiencia en investigación, docencia universitaria y práctica clínica.</p>
                    </div>
                </div>
            </div>   
            <div style={{ height:'47%', marginLeft: 'auto', marginRight: 'auto', width: '98%', fontSize: '28px', textAlign: 'justify'}}>
                <p>La mayoría de nuestros miembros cuenta con entrenamientos y certificaciones profesionales internacionales. Desde su fundación hace 11 años; se ha caracterizado por innovar en tratamientos basados en la evidencia, especializarse en el tratamiento de enfermedades afectivas resistentes, así como en la formación y certificación de profesionales de la salud mental.</p>
                <p>También en áreas complementarias al tratamiento psicoterapéutico y psicofarmacológico, como farmacia especializada, pruebas de evaluación, talleres individuales y de pareja para clientes, laboratorio del sueño portátil y clínica de neuroestimulación.</p>
                <p>Estamos comprometidos para formar un equipo de trabajo de acorde a las necesidades individuales de los clientes y sus familias que requieran asistencia de salud mental, utilizando los tratamientos más eficaces, siempre buscando alcanzar el bienestar y confianza de quiénes nos visitan.</p></div>

            <div>


            </div>

         </div>

        )
    }
}
export default Home