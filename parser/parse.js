import {collect} from 'content-structure'
import {fileURLToPath} from 'url';
import {dirname} from 'path'

await collect({
    rootdir:dirname(fileURLToPath(import.meta.url)),
    rel_contentdir:"../markdown",
    content_ext:["md","json","yml","yaml"],
    assets_ext:["svg","webp","png","jpeg","jpg","xlsx","glb"],
    rel_outdir:"../.data",
    debug:true
})
