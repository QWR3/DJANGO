export default function Airplane({item,aboutAirplane}){
    const {model, brand, id} = item
    return(
      <div>
          <h2>{id}) {brand} {model}</h2>
          <button onClick={()=> aboutAirplane(id)}>about</button>
      </div>
    );
}