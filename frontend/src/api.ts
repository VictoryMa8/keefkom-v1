// An interface describes the sahpe of an object
export interface Article {
    title: string
    publishedAt: string
    url: string
    description: string
    image: string
}

export async function fetchNews(countryCode: string): Promise<Article[]> {
    /*
    Promise<Article[]> means that this async function will eventually give us an array of Article objects

    TypeScript will then warn us if we try to use the result in a way that doesn't match
    i.e. accessing a field that doesn't exist in Article

    Without types, json.data is just "any", TS doesn't know what's in it
    */
    const response = await fetch(`/news/${countryCode}`)
    const json = await response.json()
    return json
}