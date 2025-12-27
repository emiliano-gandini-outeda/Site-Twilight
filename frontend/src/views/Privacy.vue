<template>
  <main class="privacy">
    <section class="container">
      <h1>Privacy Policy</h1>
      <p class="updated">Last updated: {{ lastUpdated }}</p>

      <section>
        <h2>1. Overview</h2>
        <p>
          Site Twilight uses Roblox authentication to identify users.
          We do not support manual registration or password-based accounts.
        </p>
      </section>

      <section>
        <h2>2. Data We Collect</h2>
        <ul>
          <li>Roblox User ID</li>
          <li>Roblox username</li>
          <li>Internal account identifiers</li>
          <li>Characters and in-site data you create</li>
        </ul>
        <p>
          We do not collect passwords, email addresses, real names, or payment information.
        </p>
      </section>

      <section>
        <h2>3. How We Use Your Data</h2>
        <ul>
          <li>Authenticate users via Roblox</li>
          <li>Create and manage user accounts</li>
          <li>Associate characters with accounts</li>
          <li>Enforce moderation and site rules</li>
          <li>Maintain security and integrity</li>
        </ul>
      </section>

      <section>
        <h2>4. Characters and Accounts</h2>
        <ul>
          <li>Users may have zero or more characters</li>
          <li>Characters are always linked to a user</li>
          <li>Deleting a character does not delete the account</li>
          <li>Deleting an account removes all associated characters</li>
        </ul>
      </section>

      <section>
        <h2>5. Data Sharing</h2>
        <p>
          We do not sell, rent, or share your data with third parties,
          except when required by law, security concerns,
          or to operate Roblox authentication.
        </p>
      </section>

      <section>
        <h2>6. Cookies and Sessions</h2>
        <p>
          We use session cookies solely for authentication and security.
          No tracking or advertising cookies are used.
        </p>
      </section>

      <section>
        <h2>7. Data Retention</h2>
        <p>
          Data is retained while your account exists.
          You may request deletion; backups may persist briefly for security reasons.
        </p>
      </section>

      <section>
        <h2>8. Security</h2>
        <p>
          We use reasonable security measures such as HTTPS and secure sessions.
          No system can guarantee absolute security.
        </p>
      </section>

      <section>
        <h2>9. Children’s Privacy</h2>
        <p>
          This site relies on Roblox authentication.
          We do not knowingly collect additional personal data from minors.
        </p>
      </section>

      <section>
        <h2>10. Policy Changes</h2>
        <p>
          This policy may be updated.
          Changes will be posted on this page.
        </p>
      </section>

      <section>
        <h2>11. Contact</h2>
        <p>
          For privacy or data deletion requests, contact:
          <strong>contact@site-twilight.com</strong>
        </p>
      </section>
    </section>
  </main>
</template>

<script setup>
const lastUpdated = "2025-01-01"
</script>

<style scoped>
.privacy {
  padding: 3rem 1rem;
  color: #e6e6e6;
  background: #0b0e13;
}

.container {
  max-width: 800px;
  margin: 0 auto;
}

h1 {
  font-size: 2.4rem;
  margin-bottom: 0.5rem;
}

.updated {
  font-size: 0.9rem;
  opacity: 0.7;
  margin-bottom: 2rem;
}

section {
  margin-bottom: 1.8rem;
}

h2 {
  font-size: 1.2rem;
  margin-bottom: 0.4rem;
}

ul {
  padding-left: 1.2rem;
}

li {
  margin-bottom: 0.3rem;
}
</style>
