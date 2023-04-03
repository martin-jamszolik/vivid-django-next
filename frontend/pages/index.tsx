import Head from 'next/head'
import Image from 'next/image'
import Link from 'next/link'
import styles from '../styles/Home.module.css'
import useSWR from 'swr'

const fetcher = (url: string) => fetch(url, {
  headers: {
    'Content-Type': 'application/json',
    'Accept': 'application/json'
  }
}).then((res) => res.json());


export default function Home() {
  const { data, error } = useSWR(
    "/api/estimations/projects/",
    fetcher
  );
  if (error) return "An error has occurred fetching API Data";
  if (!data) return "Loading...";
  return (
    <div className={styles.container}>
      <Head>
        <title>I am Next</title>
        <meta name="description" content="Next with Django" />
        <link rel="icon" href="/favicon.ico" />
      </Head>

      <main className={styles.main}>
        <p className={styles.description} >
          <h2>Client side fetched list from Django backend</h2>
          <ol>
            {data.map((pr) => (
              <li>{pr.name} - {pr.status} - {pr.url}</li>
            ))}
          </ol>
        </p>

        <div className={styles.grid}>
          <Link href="/about" className={styles.card}>
            <h2>About Page &rarr;</h2>
            <p>Cypress will test if this link is working.</p>
          </Link>

        </div>
      </main>

    </div>
  )
}
