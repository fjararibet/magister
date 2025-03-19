import viennaps2d as vps
import viennals2d as vls

vps.Logger.setLogLevel(vps.LogLevel.INFO)

domain = vps.Domain()
vps.MakeStack(domain, .21, 40., 0., 15, 2.5, 10., 0., 15., 5., False).apply()
domain.saveVolumeMesh("stack_init")

domain.duplicateTopLevelSet(vps.Material.Polymer)

model = vps.FluorocarbonEtching(50., 90., 5.5, 100., 10., 1000., 1.)
vps.Process(domain, model, 10.).apply()

domain.saveVolumeMesh("stack")

levelsets = domain.getLevelSets()

for i, ls in enumerate(levelsets):
    mesh = vls.lsMesh()
    vls.lsToSurfaceMesh(ls, mesh).apply()
    vls.lsVTKWriter(mesh, "stack_" + str(i) + ".vtp").apply()
