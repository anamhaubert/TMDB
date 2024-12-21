<script>
    import Page from "../routes/+page.svelte";

    let artists = $state(null);
    let inputContent = $state('');
    let filter = $state(1);
    let error = $state(null)

    const getArtists = (inputContent,filter)=>{
        let endpoint = `http://localhost:8000/person/search/${inputContent}`
        if(filter == 2)
            endpoint=`http://localhost:8000/person/${inputContent}`
        
        let response = fetch(endpoint, {headers:{"Content-type":"application/json"}})
        .then(res => res.json()).then(data =>{
            return data;
        })
        return response
    }
    const handleClick = async () =>{
        if(inputContent.trim() == '' || inputContent == null){
            error = "Preencha todos os campos"
        }else if (filter==2 && !parseInt(inputContent)){
            error = "Insira um ID válido" 
        } else {
            error = null;
            let data = await getArtists(inputContent,filter);
            if(data['results']){
                if(data['results'].length >0){
                    artists=data['results']
                }
                else {
                    error="Nenhum resultado encontrado"
                }
            }else{
                if (data && !data.detail){
                    artists =[data]
                }
                else {
                    error="Nenhum resultado encontrado"
                }
            }
        }
    }
</script>


<h1>Artistas</h1>
<div >
    <p>Pesquise um artista:</p>
    {#if error }
        <p id="error">{error}</p>
    {/if}
    <input type="text" onchange={(event) => inputContent = event.target.value} > 
    <select onchange={(event) => filter = (event.target.value)}>
        <option value=1>Nome</option>
        <option value=2>ID</option>
    </select>
    <button onclick={handleClick}>Pesquisar</button>
</div>
<div class="result">
    {#if artists}
    {#each artists as artist}
    <div>
        <p>ID: {artist.id}</p>
        <p>Nome: {artist.name}</p>  
        <p>Popularidade: {artist.popularity}</p>  
        <p>Departamento: {artist.known_for_department}</p>  
        <img style="width: 150px;" alt="imagem do artista" src="https://image.tmdb.org/t/p/w500/{artist.profile_path}">
    </div>
    {/each}
    {/if}
</div>

<style>
   
    h1 {
        text-align: center;
        color: #d35d90;
        font-size: 2.5rem;
        margin-top: 20px;
    }

    div {
        margin: 0 auto;
        width: 90%;
        max-width: 800px;
        text-align: center;
    }

    p {
        font-size: 1.2rem;
        margin: 10px 0;
    }

    #error {
        color: #ff4d6d;
        font-weight: bold;
    }

    input, select {
        font-size: 1rem;
        padding: 10px;
        margin: 10px;
        border: 1px solid #e8a8c7;
        border-radius: 8px;
        background-color: #ffedf7;
    }

    button {
        font-size: 1rem;
        padding: 10px 20px;
        background-color: #d35d90;
        color: white;
        border: none;
        border-radius: 8px;
        cursor: pointer;
        transition: background-color 0.3s;
    }

    button:hover {
        background-color: #b94d78;
    }

    .result {
        margin-top: 20px;
    }

    .result div {
        background-color: #ffedf7;
        border: 1px solid #e8a8c7;
        border-radius: 10px;
        padding: 15px;
        margin: 10px 0;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    }

    .result img {
        border-radius: 10px;
        margin-top: 10px;
    }
</style>

  