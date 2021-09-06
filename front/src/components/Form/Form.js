import {useEffect, useState} from "react";
import {updateAirplane} from "../../services/API";

export default function Form({item}) {
    const [formState, setFormState] = useState({...item})
    useEffect(() => {
        setFormState({...item})
        //eslint-disable-next-line
    }, [item.id])

    function onSubmit(e) {
        e.preventDefault()
        updateAirplane(formState).then(() => {
                window.location.reload()
            }
        )
    }


    function onChange(e) {
        setFormState({...formState, [e.target.name]: e.target.value})
    }

    return (
        <div>
            <form onSubmit={onSubmit}>
                <p>brand</p>
                <input type="text" name={'brand'} placeholder={'brand'} onChange={onChange} value={formState.brand}/>
                <p>model</p>
                <input type="text" name={'model'} placeholder={'model'} onChange={onChange} value={formState.model}/>
                <p>speed</p>
                <input type="number" name={'speed'} placeholder={'speed'} onChange={onChange} value={formState.speed}/>
                <p>year</p>
                <input type="number" name={'year'} placeholder={'year'} onChange={onChange} value={formState.year}/>
                <p>number of passengers</p>
                <input type="number" name={'number_of_passengers'} placeholder={'number of passengers'}
                       onChange={onChange} value={formState.number_of_passengers}/>
                <br/>
                <button>update</button>
            </form>
        </div>
    )
}