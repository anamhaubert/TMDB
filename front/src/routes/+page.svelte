<header>
    <h1>Bem-vindo ao Svelte</h1>
    <p>Explore informações sobre artistas e filmes!</p>
</header>

<main>
    <section>
        <h2>Artistas</h2>
        <p>
            Descubra detalhes fascinantes sobre seus artistas favoritos.
            Visite <a href="/artists">artistas</a> para explorar!
        </p>
    </section>
    <section>
        <h2>Filmes</h2>
        <p>
            Mergulhe no universo do cinema.
            Clique em <a href="/movies">filmes</a> para começar sua jornada!
        </p>
    </section>
</main>

<style>
      header {
        background-color: #FADADD; /* Rosa pastel */
        padding: 1rem;
        text-align: center;
        color: #355070; /* Azul pastel escuro */
        box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1);
    }

    header h1 {
        margin: 0;
        font-size: 2.5rem;
        font-weight: bold;
    }

    header p {
        margin: 0.5rem 0 0;
        font-size: 1rem;
        color: #6D597A; /* Roxo pastel */
    }

    main {
        margin: 2rem auto;
        padding: 2rem;
        max-width: 800px;
        background-color: #FFE5EC; /* Rosa claro */
        border-radius: 10px;
        box-shadow: 0px 2px 4px rgba(0, 0, 0, 0.1);
    }

    section {
        margin-bottom: 2rem;
    }

    section h2 {
        font-size: 2rem;
        color: #B56576; /* Rosa pastel escuro */
        border-bottom: 2px solid #6D597A; /* Roxo pastel */
        padding-bottom: 0.5rem;
    }

    section p {
        font-size: 1rem;
        line-height: 1.6;
        color: #355070; /* Azul pastel escuro */
    }

    a {
        color: #B56576;
        text-decoration: none;
        font-weight: bold;
    }

    a:hover {
        color: #6D597A;
    }
</style>


