import Head from "next/head";
import Image from "next/image";
import { Geist, Geist_Mono } from "next/font/google";
import styles from "@/styles/Home.module.css";

const geistSans = Geist({
  variable: "--font-geist-sans",
  subsets: ["latin"],
});

const geistMono = Geist_Mono({
  variable: "--font-geist-mono",
  subsets: ["latin"],
});

export default function Home() {
  return (
    <>
      <Head>
        <title>ESLSCA Courses</title>
        <meta name="description" content="Links for ESLSCA courses" />
        <meta name="viewport" content="width=device-width, initial-scale=1" />
        <link rel="icon" href="/favicon.ico" />
      </Head>
      <div className={`${styles.page} ${geistSans.variable} ${geistMono.variable}`}>
        <main className={styles.main}>
          {/* <a className={styles.links} href="/cours_architecture_nosql.pdf" download="cours_architecture_nosql.pdf">- Cours Architecture NoSQL.pdf</a> */}
          <a className={styles.links} href="/dev_web_01.pdf" download="dev_web_01.pdf">- Cours Dev Web 1.pdf</a>
          <a className={styles.links} href="/dev_web_02.pdf" download="dev_web_02.pdf">- Cours Dev Web 1.pdf</a>
          <a className={styles.links} href="/nodejs_lesbases.pdf" download="nodejs_lesbases.pdf">- NodeJS - Les Bases.pdf</a>
          {/* <a className={styles.links} href="/cours_db_ns.pdf" download="cours_db_ns.pdf">- Cours DB NS.pdf</a>
          <a className={styles.links} href="/nsdb.txt" download="nsdb.txt">- NSDB.txt</a>
          <a className={styles.links} href="/script.py" download="script.py">- Script.py</a> */}
        </main>
      </div>
    </>
  );
}
