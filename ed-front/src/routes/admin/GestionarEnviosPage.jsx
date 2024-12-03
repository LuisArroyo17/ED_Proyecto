import { TitleAdmin } from "../../components/TitleAdmin";
import EnvioQueuePage from "../../routes/EnvioQueuePage";

export function GestionarEnviosPage() {
  return (
    <section className="w-[80%] flex flex-col gap-10">
      <TitleAdmin title="Gestionar Envíos" />
      <EnvioQueuePage />
    </section>
  );
}
