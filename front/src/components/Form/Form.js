import {useEffect, useState} from "react";
import {createAirplane, updateAirplane} from "../../services/API";

export default function Form({item, do_you_wont_update_component}) {
    const [formState, setFormState] = useState({...item})
    useEffect(() => {
        setFormState({...item})
        // eslint-disable-next-line
    }, [item?.id])

    function onSubmit(e) {
        e.preventDefault()
        if (do_you_wont_update_component) {
            updateAirplane(formState).then(() => {
                    window.location.reload()
                }
            )
        } else {
            console.log(formState)
            createAirplane(formState).then(() => {
                window.location.reload()
            })
        }
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
                <p>max range of flight</p>
                <input type="number" name={'max_range_of_flight'} placeholder={'max range of flight'}
                       onChange={onChange} value={formState.max_range_of_flight}/>
                <br/>
                {do_you_wont_update_component && <button>update</button>}
                {!do_you_wont_update_component && <button>create</button>}
            </form>
        </div>
    )
}