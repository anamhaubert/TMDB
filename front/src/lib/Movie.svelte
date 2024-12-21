<script>

let results = $state(null);

async function getMovies() {
    let endpoint = `http://localhost:8000/movies/top`;
    const res = await fetch(endpoint);
    const data = await res.json();

        if (res.ok) {
            return data;
        } else {throw new Error(data); } 
    }

function handleClick() {
    getMovies().then((data)=>{
        results = data["results"];
    });
    }
</script>

<div class="container">
    <h1>Top 20 Filmes</h1>
  
    <button onclick={handleClick}>
      Listar Filmes
    </button>
  
    <div class="results">
      {#if results}
        {#each results as movie}
          <div class="movie-card">
            <p class="movie-title">Título: {movie.title}</p>
            <p class="movie-release">
              Ano: {new Date(movie.release_date).toLocaleDateString('pt-br')}
            </p>
          </div>
        {/each}
      {/if}
    </div>
  </div>

  <style>

    .container {
        text-align: center;
        padding: 2rem;
    }

    .container h1 {
        font-size: 2.5rem;
        color: #B56576; /* Rosa pastel escuro */
        margin-bottom: 1rem;
    }

    .container button {
        background-color: #FADADD; /* Rosa pastel */
        color: #355070; /* Azul pastel escuro */
        font-size: 1rem;
        padding: 0.75rem 1.5rem;
        border: none;
        border-radius: 5px;
        cursor: pointer;
        font-weight: bold;
        transition: background-color 0.3s, transform 0.3s;
        box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1); /* Sombra leve */
    }

    .container button:hover {
        background-color: #FFE5EC; /* Rosa mais claro */
        transform: scale(1.05); /* Cresce levemente */
    }

    .container button:active {
        background-color: #B56576; /* Rosa pastel escuro */
        color: #FFF7F9; /* Branco pastel */
    }

    .results {
        margin-top: 2rem;
        display: flex;
        flex-wrap: wrap;
        justify-content: center;
        gap: 1.5rem;
    }

    .movie-card {
        background-color: #FFE5EC; /* Rosa claro */
        border: 1px solid #FADADD; /* Rosa pastel */
        border-radius: 10px;
        padding: 1rem;
        width: 250px;
        box-shadow: 0px 2px 4px rgba(0, 0, 0, 0.1); /* Sombra leve */
        text-align: left;
    }

    .movie-title {
        font-size: 1.2rem;
        font-weight: bold;
        color: #B56576; /* Rosa pastel escuro */
        margin-bottom: 0.5rem;
    }

    .movie-release {
        font-size: 1rem;
        color: #355070; /* Azul pastel escuro */
    }
</style>