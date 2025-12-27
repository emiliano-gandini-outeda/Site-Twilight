<template>
  <main class="tos">
    <section class="container">
      <h1>Terms of Service</h1>
      <p class="updated">Last updated: {{ lastUpdated }}</p>

      <section>
        <h2>1. Acceptance of Terms</h2>
        <p>
          By accessing or using Site Twilight, you agree to these Terms of Service.
          If you do not agree, do not use the site.
        </p>
      </section>

      <section>
        <h2>2. Accounts and Authentication</h2>
        <ul>
          <li>Accounts are created exclusively through Roblox authentication</li>
          <li>No manual registration or passwords are supported</li>
          <li>You are responsible for activity on your account</li>
        </ul>
      </section>

      <section>
        <h2>3. User Accounts and Characters</h2>
        <ul>
          <li>Users may have zero or more characters</li>
          <li>Characters are always linked to a user account</li>
          <li>Deleting a character does not delete the account</li>
          <li>Deleting an account removes all associated characters</li>
        </ul>
      </section>

      <section>
        <h2>4. User Conduct</h2>
        <p>You agree not to:</p>
        <ul>
          <li>Exploit bugs or unintended mechanics</li>
          <li>Impersonate other users</li>
          <li>Harass, threaten, or abuse others</li>
          <li>Attempt unauthorized system access</li>
          <li>Evade moderation actions</li>
        </ul>
      </section>

      <section>
        <h2>5. Moderation</h2>
        <p>
          Moderators and administrators may enforce rules through warnings,
          restrictions, character removal, or account bans.
          Moderation decisions are final.
        </p>
      </section>

      <section>
        <h2>6. Content and Roleplay</h2>
        <p>
          Users are responsible for their content.
          We may remove content that violates rules or disrupts the service.
        </p>
      </section>

      <section>
        <h2>7. Service Availability</h2>
        <p>
          The service is provided “as is” and may be modified or discontinued
          at any time without notice.
        </p>
      </section>

      <section>
        <h2>8. Termination</h2>
        <p>
          We may suspend or terminate access for violations of these Terms
          or to protect the platform.
        </p>
      </section>

      <section>
        <h2>9. Limitation of Liability</h2>
        <p>
          We are not liable for data loss, service interruptions,
          or damages arising from use of the service.
        </p>
      </section>

      <section>
        <h2>10. Changes to These Terms</h2>
        <p>
          These Terms may be updated at any time.
          Continued use constitutes acceptance.
        </p>
      </section>

      <section>
        <h2>11. Contact</h2>
        <p>
          Questions regarding these Terms can be sent to:
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
.tos {
  padding: 3rem 1rem;
  background: #0b0e13;
  color: #e6e6e6;
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
